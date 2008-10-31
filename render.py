#!/usr/bin/env python
#
# phpMyAdmin web site generator
#
# Copyright (C) 2008 Michal Cihar <michal@cihar.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import sys
import os
import feedparser
import re
import cPickle
import glob
from genshi.template import TemplateLoader
from genshi.template import NewTextTemplate


# Project part
PROJECT_ID = 23067
PROJECT_NAME = 'phpmyadmin'

# Filtering
FILES_FILTER = [('phpMyAdmin', True), ('theme', False)]
FILES_MARK = 'all-languages.'
BRANCH_REGEXP = re.compile('^([0-9]+\.[0-9]+)\.')
SIZE_REGEXP = re.compile('.*\(([0-9]+) bytes, ([0-9]+) downloads to date')

# Base URL (including trailing /)
BASE_URL = '/mcihar/phpmyadmin/output/'
BASE_URL = '/'

# Main menu
MENU = [
    ('', 'About'),
    ('news', 'News'),
    ('security/', 'Security'),
    ('screenshots', 'Screenshots'),
    ('translations', 'Translations'),
    ('themes', 'Themes'),
    ('download', 'Download'),
]

# File locations
TEMPLATES = './templates'
CSS = './css'
OUTPUT = './output'

# Generic sourceforge.net part
PROJECT_FILES_RSS = 'https://sourceforge.net/export/rss2_projfiles.php?group_id=%d&rss_limit=100' % PROJECT_ID
PROJECT_NEWS_RSS = 'https://sourceforge.net/export/rss2_projnews.php?group_id=%d&rss_fulltext=1&limit=10' % PROJECT_ID
DONATIONS_RSS = 'https://sourceforge.net/export/rss2_projdonors.php?group_id=%d&limit=20' % PROJECT_ID
PROJECT_DL = 'http://prdownloads.sourceforge.net/%s/%%s?download' % PROJECT_NAME

VERBOSE = True


def dbg(text):
    if VERBOSE:
        sys.stderr.write(text)
        sys.stderr.write('\n')

class SFGenerator:
    def __init__(self, templates = [TEMPLATES], css = [CSS]):
        self.data = {
            'files': {},
            'news': [],
            'donations': [],
            'base_url': BASE_URL,
            }
        for filetype in FILES_FILTER:
            self.data['files'][filetype[0]] = []
        self.loader = TemplateLoader(templates)
        self.cssloader = TemplateLoader(css, default_class = NewTextTemplate)

    def get_feed(self, name, url):
        dbg('Downloading and parsing %s feed...' % name)
        dbg('URL: %s' % url)
        try:
            result = cPickle.load(open('./cache/feed-%s.dump' % name, 'r'))
        except IOError:
            result = feedparser.parse(url)
            cPickle.dump(result, open('./cache/feed-%s.dump' % name, 'w'))
        return result

    def process_releases(self, rss_downloads):
        dbg('Processing releases feed...')
        for entry in rss_downloads.entries:
            titleparts = entry.title.split(' ')
            type = titleparts[0]
            version = titleparts[1]
            release = {}
            release['show'] = False
            release['notes'] = entry.link
            release['version'] = version
            release['date'] = entry.updated
            release['name'] = '%s %s' % (type, version)
            text = entry.summary
            fileslist = text[text.find('Includes files:') + 15:]
            fileslist = fileslist[:fileslist.find('<br />')]
            release['files'] = []
            for part in fileslist.split('),'):
                m = SIZE_REGEXP.match(part)
                size = m.group(1)
                dlcount = m.group(2)
                filename = part.strip().split(' ')[0]
                url = PROJECT_DL % filename
                ext = os.path.splitext(filename)[1]
                mark = (filename.find(FILES_MARK) != -1)
                release['files'].append({'name': filename, 'url': url, 'ext': ext, 'mark': mark, 'size': size, 'dlcount': dlcount})
            found = False
            for filetype in FILES_FILTER:
                if filetype[0] == type[:len(filetype[0])]:
                    self.data['files'][filetype[0]].append(release)
                    found = True
                    break
            if not found:
                print 'Not matched file type: %s' % type

        dbg('Sorting file lists...')
        self.data['files']['phpMyAdmin'].sort(key = lambda x: x['version'], reverse = True)
        self.data['files']['theme'].sort(key = lambda x: x['name'])

        dbg('Detecting actual versions...')
        for filetype in FILES_FILTER:
            if not filetype[1]:
                continue
            outversions = {}
            for idx in xrange(len(self.data['files'][filetype[0]])):
                version = self.data['files'][filetype[0]][idx]
                branch = BRANCH_REGEXP.match(version['version']).group(1)
                try:
                    if self.data['files'][filetype[0]][outversions[branch]]['version'] < version['version']:
                        outversions[branch] = idx
                except KeyError:
                    outversions[branch] = idx

            newlist = {}
            dbg('Actual versions detected:')
            for version in outversions.values():
                dbg('  %s' % self.data['files'][filetype[0]][version]['version'])
                self.data['files'][filetype[0]][version]['show'] = True

    def process_news(self, feed):
        dbg('Processing news feed...')
        for entry in feed.entries:
            item = {}
            item['link'] = entry.link
            item['date'] = entry.updated
            item['text'] = entry.summary
            item['title'] = entry.title
            self.data['news'].append(item)

    def process_donations(self, feed):
        dbg('Processing news feed...')
        for entry in feed.entries:
            item = {}
            item['link'] = entry.link
            item['date'] = entry.updated
            item['text'] = entry.summary
            item['title'] = entry.title
            self.data['donations'].append(item)

    def get_menu(self, active):
        menu = []
        for item in MENU:
            title = item[1]
            name = item[0]
            field = {
                'title' : title,
                'class' : {},
            }
            if name == active or '%sindex' % name == active:
                field['class'] = { 'class': 'active' }
            if len(name) > 0 and name[-1] != '/':
                name = '%s.html' % name
            field['link'] = '%s%s' % (BASE_URL, name)
            menu.append(field)
        return menu

    def render_css(self, filename):
        dbg('  %s' % filename)
        template = self.cssloader.load(filename)
        out = open(os.path.join(OUTPUT, 'css', filename), 'w')
        out.write(template.generate(**self.data).render())
        out.close()

    def render(self, page):
        dbg('  %s' % page)
        template = self.loader.load('%s.tpl' % page)
        menu = self.get_menu(page)
        out = open(os.path.join(OUTPUT, '%s.html' % page), 'w')
        out.write(template.generate(menu = menu, **self.data).render('xhtml'))
        out.close()

    def render_security(self, issue):
        dbg('  %s' % issue)
        content = unicode(open('templates/security/%s' % issue, 'r').read(), 'utf-8')
        template = self.loader.load('security/_page.tpl')
        menu = self.get_menu('security/')
        out = open(os.path.join(OUTPUT, 'security', '%s.html' % issue), 'w')
        #
        out.write(template.generate(menu = menu, issue = issue, content = content, **self.data).render('xhtml'))
        out.close()


    def list_security_issues(self):
        issues = glob.glob('templates/security/PMASA*')
        issues.sort(reverse = True)
        issues = [os.path.basename(x) for x in issues]
        self.data['issues'] = [{'name' : x, 'link': '%ssecurity/%s.html' % (BASE_URL, x)} for x in issues]

    def main(self):
        rss_downloads = self.get_feed('releases', PROJECT_FILES_RSS)
        self.process_releases(rss_downloads)

        rss_news = self.get_feed('news', PROJECT_NEWS_RSS)
        self.process_news(rss_news)

        rss_donations = self.get_feed('donations', DONATIONS_RSS)
        self.process_donations(rss_donations)

        self.list_security_issues()

        dbg('Rendering pages:')
        templates = [os.path.basename(x) for x in glob.glob('templates/*.tpl')]
        templates.extend([os.path.join('security', os.path.basename(x)) for x in glob.glob('templates/security/*.tpl')])
        for template in templates:
            name = os.path.splitext(template)[0]
            if os.path.basename(name)[0] == '_':
                continue
            self.render(name)

        dbg('Rendering security issues pages:')
        for issue in self.data['issues']:
            self.render_security(issue['name'])

        self.render_css('style.css')

        dbg('Done!')

if __name__ == '__main__':
    gen = SFGenerator()
    gen.main()
