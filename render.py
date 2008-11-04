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
import shutil
import datetime
import time
from genshi.template import TemplateLoader
from genshi.template import NewTextTemplate
from genshi.input import XML

import md5sums

# Project part
PROJECT_ID = 23067
PROJECT_NAME = 'phpmyadmin'

# Filtering
FILES_MARK = 'all-languages.'
BRANCH_REGEXP = re.compile('^([0-9]+\.[0-9]+)\.')
SIZE_REGEXP = re.compile('.*\(([0-9]+) bytes, ([0-9]+) downloads to date')
COMMENTS_REGEXP = re.compile('^(.*)\(<a href="([^"]*)">([0-9]*) comments</a>\)$')

# Base URL (including trailing /)
SERVER = 'http://new.cihar.com'
BASE_URL = '/'
EXTENSION = 'html'

# Main menu
MENU = [
    ('', 'About'),
    ('news', 'News'),
    ('security/', 'Security'),
    ('support', 'Support'),
    ('docs', 'Docs'),
    ('try', 'Try'),
    ('improve', 'Improve'),
    ('themes', 'Themes'),
    ('download', 'Download'),
]

# List of screenshots
SCREENSHOTS = [
    {'name': 'main_page', 'title': 'Main page screenshot'},
    ]

# How many security issues are shown in RSS
TOP_ISSUES = 10

# How long is cache valid (in seconds)
CACHE_TIME = 60 * 60

# File locations
TEMPLATES = './templates'
CSS = './css'
JS = './js'
IMAGES = './images'
OUTPUT = './output'

# Generic sourceforge.net part
PROJECT_FILES_RSS = 'https://sourceforge.net/export/rss2_projfiles.php?group_id=%d&rss_limit=100' % PROJECT_ID
PROJECT_NEWS_RSS = 'https://sourceforge.net/export/rss2_projnews.php?group_id=%d&rss_fulltext=1&limit=10' % PROJECT_ID
DONATIONS_RSS = 'https://sourceforge.net/export/rss2_projdonors.php?group_id=%d&limit=20' % PROJECT_ID
PROJECT_DL = 'http://prdownloads.sourceforge.net/%s/%%s?download' % PROJECT_NAME

VERBOSE = True

class basedatetime(datetime.datetime):
    def w3cdtf(self):
        return self.strftime('%Y-%m-%dT%H:%M:%S+00:00')

class fmtdate(basedatetime):
    def __str__(self):
        return self.strftime('%a, %d %b %Y')

    def parse(text):
        return basedatetime.strptime(text.strip(), '%Y-%m-%d')
    parse = staticmethod(parse)

class fmtdatetime(basedatetime):
    def __str__(self):
        return self.strftime('%a, %d %b %Y %H:%M:%S GMT')

    def parse(text):
        return basedatetime.strptime(text, '%a, %d %b %Y %H:%M:%S %Z')
    parse = staticmethod(parse)

def warn(text):
    sys.stderr.write('%s\n' % text)

def dbg(text):
    if VERBOSE:
        sys.stderr.write('%s\n' % text)

class SFGenerator:
    def __init__(self, templates = [TEMPLATES], css = [CSS], js = [JS]):
        self.data = {
            'releases': [],
            'releases_older': [],
            'themes': [],
            'news': [],
            'issues': [],
            'donations': [],
            'base_url': BASE_URL,
            'server': SERVER,
            'file_ext': EXTENSION,
            'rss_files': PROJECT_FILES_RSS,
            'rss_donations': DONATIONS_RSS,
            'rss_news': PROJECT_NEWS_RSS,
            'screenshots': SCREENSHOTS,
            'generated': fmtdatetime.utcnow(),
            }
        self.loader = TemplateLoader(templates)
        self.cssloader = TemplateLoader(css, default_class = NewTextTemplate)
        self.jsloader = TemplateLoader(js, default_class = NewTextTemplate)

    def get_feed(self, name, url):
        dbg('Downloading and parsing %s feed...' % name)
        dbg('URL: %s' % url)
        cache = './cache/feed-%s.dump' % name
        try:
            mtime = os.path.getmtime(cache)
        except OSError:
            mtime = 0
        if mtime + CACHE_TIME > time.time():
            dbg('Using cache!')
            result = cPickle.load(open(cache, 'r'))
        else:
            result = feedparser.parse(url)
            cPickle.dump(result, open(cache, 'w'))
        return result

    def get_outname(self, page):
        '''
        Converts page name to file name. Basically only extension is appended
        if none is already used.
        '''
        if page.find('.') == -1:
            return '%s.%s' % (page, EXTENSION)
        else:
            return page

    def get_renderer(self, page):
        '''
        Returns genshi renderer type for chosen page.
        '''
        if page[:-4] == '.xml':
            return 'xml'
        return 'xhtml'

    def text_to_id(self, text):
        '''
        Converts text to something what can be used as a anchor or id (no spaces
        or other special chars).
        '''
        return re.sub('[^a-z0-9A-Z.-]', '_', text)

    def process_releases(self, rss_downloads):
        '''
        Gets phpMyAdmin releases out of releases feed and fills releases
        and releases_older.
        '''
        dbg('Processing file releases...')
        releases = []
        for entry in rss_downloads.entries:
            titleparts = entry.title.split(' ')
            type = titleparts[0]
            if type != 'phpMyAdmin':
                continue
            version = titleparts[1]
            release = {}
            release['show'] = False
            release['notes'] = entry.link
            release['version'] = version
            release['date'] = fmtdatetime.parse(entry.updated)
            release['name'] = type
            release['fullname'] = '%s %s' % (type, version)
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
                featured = (filename.find(FILES_MARK) != -1)
                try:
                    md5 = md5sums.md5sum[filename]
                except KeyError:
                    md5 = 'N/A'
                release['files'].append({'name': filename, 'url': url, 'ext': ext, 'featured': featured, 'size': size, 'dlcount': dlcount, 'md5': md5})
            releases.append(release)

        dbg('Sorting file lists...')
        releases.sort(key = lambda x: x['version'], reverse = True)

        dbg('Detecting actual versions...')
        outversions = {}
        for idx in xrange(len(releases)):
            version = releases[idx]
            branch = BRANCH_REGEXP.match(version['version']).group(1)
            try:
                if releases[outversions[branch]]['version'] < version['version']:
                    outversions[branch] = idx
            except KeyError:
                outversions[branch] = idx

        dbg('Actual versions detected:')
        for idx in xrange(len(releases)):
            if idx in outversions.values():
                self.data['releases'].append(releases[idx])
            else:
                self.data['releases_older'].append(releases[idx])

    def process_themes(self, rss_downloads):
        '''
        Gets theme releases out of releases feed and fills themes.
        '''
        dbg('Processing themes releases...')
        for entry in rss_downloads.entries:
            titleparts = entry.title.split(' ')
            type = titleparts[0]
            if type[:6] != 'theme-':
                continue
            type = type[6:]
            version = titleparts[1]
            release = {}
            release['show'] = False
            release['notes'] = entry.link
            release['version'] = version
            release['date'] = fmtdatetime.strptime(entry.updated, '%a, %d %b %Y %H:%M:%S %Z')
            release['name'] = type
            release['fullname'] = '%s %s' % (type, version)
            text = entry.summary
            fileslist = text[text.find('Includes files:') + 15:]
            fileslist = fileslist[:fileslist.find('<br />')]
            files = fileslist.split('),')
            if len(files) > 1:
                raise Exception('Too much files in theme %s' % type)
            part = files[0]
            m = SIZE_REGEXP.match(part)
            size = m.group(1)
            dlcount = m.group(2)
            filename = part.strip().split(' ')[0]
            url = PROJECT_DL % filename
            ext = os.path.splitext(filename)[1]
            mark = (filename.find(FILES_MARK) != -1)
            release['file'] = {'name': filename, 'url': url, 'ext': ext, 'mark': mark, 'size': size, 'dlcount': dlcount}
            self.data['themes'].append(release)

        dbg('Sorting file lists...')
        self.data['themes'].sort(key = lambda x: x['name'])

    def process_news(self, feed):
        '''
        Fills in news based on news feed.
        '''
        dbg('Processing news feed...')
        for entry in feed.entries:
            matches = COMMENTS_REGEXP.match(entry.summary)
            item = {}
            item['link'] = entry.link
            item['date'] = fmtdatetime.strptime(entry.updated, '%a, %d %b %Y %H:%M:%S %Z')
            item['text'] = matches.group(1)
            item['comments_link'] = matches.group(2)
            item['comments_number'] = matches.group(3)
            item['title'] = entry.title
            item['anchor'] = self.text_to_id(entry.title)
            self.data['news'].append(item)

    def process_donations(self, feed):
        '''
        Fills in donations based on donations feed.
        '''
        dbg('Processing news feed...')
        for entry in feed.entries:
            item = {}
            item['link'] = entry.link
            item['date'] = fmtdatetime.strptime(entry.updated, '%a, %d %b %Y %H:%M:%S %Z')
            item['text'] = entry.summary
            item['title'] = entry.title
            self.data['donations'].append(item)

    def get_menu(self, active):
        '''
        Returns list of menu entries with marked active one.
        '''
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
                name = self.get_outname(name)
            field['link'] = '%s%s' % (BASE_URL, name)
            menu.append(field)
        return menu

    def render_css(self, filename):
        '''
        Renders CSS file from template.
        '''
        dbg('  %s' % filename)
        template = self.cssloader.load(filename)
        out = open(os.path.join(OUTPUT, 'css', filename), 'w')
        out.write(template.generate(**self.data).render())
        out.close()

    def render_js(self, filename):
        '''
        Renders JavaScript file from template. Some defined files are not processed
        through template engine as they were taken from other projects.
        '''
        dbg('  %s' % filename)
        outpath = os.path.join(OUTPUT, 'js', filename)
        if filename in ['mootools.js', 'slimbox.js', 'fader.js']:
            shutil.copy(os.path.join(JS, filename), outpath)
            return
        template = self.jsloader.load(filename)
        out = open(outpath, 'w')
        out.write(template.generate(**self.data).render())
        out.close()

    def render(self, page):
        '''
        Renders standard page.
        '''
        dbg('  %s' % page)
        template = self.loader.load('%s.tpl' % page)
        menu = self.get_menu(page)
        out = open(os.path.join(OUTPUT, self.get_outname(page)), 'w')
        out.write(template.generate(menu = menu, **self.data).render(self.get_renderer(page)))
        out.close()

    def render_security(self, issue):
        '''
        Renders security issue.
        '''
        dbg('  %s' % issue)
        template = self.loader.load('security/%s' % issue)
        menu = self.get_menu('security/')
        out = open(os.path.join(OUTPUT, 'security', self.get_outname(issue)), 'w')
        out.write(template.generate(menu = menu, issue = issue, **self.data).render('xhtml'))
        out.close()


    def list_security_issues(self):
        '''
        Fills in issues and topissues with security issues information.
        '''
        issues = glob.glob('templates/security/PMASA*')
        issues.sort(reverse = True)
        for issue in issues:
            data = XML(open(issue, 'r').read())
            name = os.path.basename(issue)
            self.data['issues'].append({
                'name' : name,
                'link': '%ssecurity/%s' % (BASE_URL, self.get_outname(name)),
                'fulllink': '%s%ssecurity/%s' % (SERVER, BASE_URL, self.get_outname(name)),
                'summary': str(data.select('def[@function="announcement_summary"]/text()')),
                'date': fmtdate.parse(str(data.select('def[@function="announcement_date"]/text()'))),
            })
        self.data['topissues'] = self.data['issues'][:TOP_ISSUES]

    def prepare_output(self):
        '''
        Copies static content to output and creates required directories.
        '''
        dbg('Copying static content to output...')
        try:
            shutil.rmtree(os.path.join(OUTPUT, 'images'))
        except OSError:
            pass
        shutil.copytree(IMAGES, os.path.join(OUTPUT, 'images'))
        try:
            os.mkdir(os.path.join(OUTPUT, 'security'))
        except OSError:
            pass
        try:
            os.mkdir(os.path.join(OUTPUT, 'css'))
        except OSError:
            pass
        try:
            os.mkdir(os.path.join(OUTPUT, 'js'))
        except OSError:
            pass

    def fetch_data(self):
        '''
        Fetches data from remote or local sources and prepares template data.
        '''
        rss_downloads = self.get_feed('releases', PROJECT_FILES_RSS)
        self.process_releases(rss_downloads)
        self.process_themes(rss_downloads)

        rss_news = self.get_feed('news', PROJECT_NEWS_RSS)
        self.process_news(rss_news)

        rss_donations = self.get_feed('donations', DONATIONS_RSS)
        self.process_donations(rss_donations)

        self.list_security_issues()

    def render_pages(self):
        '''
        Renders all content pages.
        '''
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

        for css in [os.path.basename(x) for x in glob.glob('css/*.css')]:
            self.render_css(css)

        for js in [os.path.basename(x) for x in glob.glob('js/*.js')]:
            self.render_js(js)


    def main(self):
        '''
        Main program which does everything.
        '''
        self.prepare_output()
        self.fetch_data()
        self.render_pages()
        dbg('Done!')

if __name__ == '__main__':
    gen = SFGenerator()
    gen.main()
