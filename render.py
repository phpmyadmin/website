#!/usr/bin/env python
# -*- coding: UTF-8 -*-
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
import csv
import urllib
from genshi.template import TemplateLoader
from genshi.template import NewTextTemplate
from genshi.input import XML

import md5sums
import awards
import themes

# Project part
PROJECT_ID = 23067
PROJECT_NAME = 'phpmyadmin'

# Filtering
FILES_MARK = 'all-languages.'
BRANCH_REGEXP = re.compile('^([0-9]+\.[0-9]+)\.')
TESTING_REGEXP = re.compile('.*(beta|alpha|rc).*')
SIZE_REGEXP = re.compile('.*\(([0-9]+) bytes, ([0-9]+) downloads to date')
COMMENTS_REGEXP = re.compile('^(.*)\(<a href="([^"]*)">([0-9]*) comments</a>\)$')

# Base URL (including trailing /)
SERVER = 'http://www.phpmyadmin.net'
SERVER = 'http://new.cihar.com'
BASE_URL = '/test/'
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
    {'name': 'main-page', 'title': 'Main page screenshot'},
    {'name': 'main-page-rtl', 'title': 'RTL language with Darkblue/orange theme'},
    {'name': 'designer', 'title': 'Database designer'},
    {'name': 'sql-export', 'title': 'SQL export options'},
    {'name': 'privileges', 'title': 'Setting per column privileges for table'},
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

# Which JS files are not templates
JS_TEMPLATES = []

# Generic sourceforge.net part
PROJECT_FILES_RSS = 'https://sourceforge.net/export/rss2_projfiles.php?group_id=%d&rss_limit=100' % PROJECT_ID
PROJECT_NEWS_RSS = 'https://sourceforge.net/export/rss2_projnews.php?group_id=%d&rss_fulltext=1&limit=10' % PROJECT_ID
DONATIONS_RSS = 'https://sourceforge.net/export/rss2_projdonors.php?group_id=%d&limit=20' % PROJECT_ID
PROJECT_DL = 'http://prdownloads.sourceforge.net/%s/%%s?download' % PROJECT_NAME
TRANSLATION_STATS_URL = 'http://cihar.com/phpMyAdmin/translations/dump.php'

# Enable verbose messages?
VERBOSE = True
# Clean output before generating
CLEAN_OUTPUT = True

class basedatetime(datetime.datetime):
    def w3cdtf(self):
        return self.strftime('%Y-%m-%dT%H:%M:%S+00:00')

class fmtdate(basedatetime):
    def __str__(self):
        return self.strftime('%Y-%m-%d')

    def parse(text):
        return fmtdate.strptime(text.strip(), '%Y-%m-%d')
    parse = staticmethod(parse)

class fmtdatetime(basedatetime):
    def __str__(self):
        return self.strftime('%a, %d %b %Y %H:%M:%S GMT')

    def parse(text):
        return fmtdatetime.strptime(text, '%a, %d %b %Y %H:%M:%S %Z')
    parse = staticmethod(parse)

class NoCache(Exception):
    pass

def warn(text):
    sys.stderr.write('%s\n' % text)

def dbg(text):
    if VERBOSE:
        sys.stderr.write('%s\n' % text)

def copytree(src, dst):
    '''
    Trimmed down version of shutil.copytree. Recursively copies a directory
    tree using shutil.copy2().

    The destination directory must not already exist.
    If exception(s) occur, an Error is raised with a list of reasons.

    It handles only files and dirs and ignores .svn and *.swp* files.
    '''
    names = os.listdir(src)
    os.makedirs(dst)
    errors = []
    for name in names:
        if name == '.svn' or name.find('.swp') != -1:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.isdir(srcname):
                copytree(srcname, dstname)
            else:
                shutil.copy2(srcname, dstname)
        except (IOError, os.error), why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except OSError, err:
            errors.extend(err.args[0])
    if errors:
        raise OSError, errors

class SFGenerator:
    def __init__(self):
        self.data = {
            'releases': [],
            'releases_older': [],
            'releases_beta': [],
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
            'awards': awards.AWARDS,
            'generated': fmtdatetime.utcnow(),
            'themecssversions': themes.CSSVERSIONS,
            }
        self.loader = TemplateLoader([TEMPLATES])
        self.cssloader = TemplateLoader([CSS], default_class = NewTextTemplate)
        self.jsloader = TemplateLoader([JS], default_class = NewTextTemplate)

    def get_cache_name(self, name):
        '''
        Returns cache filename for given name.
        '''
        return os.path.join('.', 'cache', '%s.dump' % name)

    def load_cache(self, name):
        '''
        Loads cache if it is available and valid, raises exception otherwise.
        '''
        filename = self.get_cache_name(name)
        try:
            mtime = os.path.getmtime(filename)
        except OSError:
            mtime = 0
        if mtime + CACHE_TIME > time.time():
            dbg('Using cache for %s!' % name)
            return cPickle.load(open(filename, 'r'))
        raise NoCache()

    def save_cache(self, name, data):
        '''
        Saves cache.
        '''
        filename = self.get_cache_name(name)
        cPickle.dump(data, open(filename, 'w'))


    def get_feed(self, name, url):
        dbg('Downloading and parsing %s feed...' % name)
        dbg('URL: %s' % url)
        cache = 'feed-%s' % name
        try:
            result = self.load_cache(cache)
        except NoCache:
            result = feedparser.parse(url)
            self.save_cache(cache, result)
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
        Gets phpMyAdmin releases out of releases feed and fills releases,
        releases_beta and releases_older.
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

        dbg('Detecting versions...')
        outversions = {}
        outbetaversions = {}

        for idx in xrange(len(releases)):
            version = releases[idx]
            branch = BRANCH_REGEXP.match(version['version']).group(1)
            test = TESTING_REGEXP.match(version['version'])
            if test is not None:
                try:
                    if releases[outbetaversions[branch]]['version'] < version['version']:
                        outbetaversions[branch] = idx
                except KeyError:
                    outbetaversions[branch] = idx
            else:
                try:
                    if releases[outversions[branch]]['version'] < version['version']:
                        outversions[branch] = idx
                except KeyError:
                    outversions[branch] = idx

        for beta in outbetaversions.keys():
            try:
                if releases[outversions[beta]]['version'] > releases[outbetaversions[beta]]['version']:
                    dbg('Old beta: %s' % releases[outbetaversions[beta]]['version'])
                    del outbetaversions[beta]
            except KeyError:
                pass

        dbg('Versions detected:')
        for idx in xrange(len(releases)):
            if idx in outversions.values():
                self.data['releases'].append(releases[idx])
                dbg(' %s' % releases[idx]['version'])
            elif idx in outbetaversions.values():
                self.data['releases_beta'].append(releases[idx])
                dbg(' beta: %s' % releases[idx]['version'])
            else:
                self.data['releases_older'].append(releases[idx])
                dbg(' old: %s' % releases[idx]['version'])

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
            release['shortname'] = type
            release['imgname'] = 'images/themes/%s.png' % type
            try:
                release.update(themes.THEMES['%s-%s' % (type, version)])
            except KeyError:
                warn('No meatadata for theme %s-%s!' % (type, version))
                release['name'] = type
                release['support'] = 'N/A'
                release['info'] = ''
            release['fullname'] = '%s %s' % (release['name'], version)
            release['classes'] = themes.CSSMAP[release['support']]

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
        self.data['themes'].sort(key = lambda x: x['date'], reverse = True)

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
        if filename not in JS_TEMPLATES:
            shutil.copy2(os.path.join(JS, filename), outpath)
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
                'cve': str(data.select('def[@function="announcement_cve"]/text()')),
            })
        self.data['topissues'] = self.data['issues'][:TOP_ISSUES]

    def prepare_output(self):
        '''
        Copies static content to output and creates required directories.
        '''
        dbg('Copying static content to output...')
        if CLEAN_OUTPUT:
            try:
                shutil.rmtree(OUTPUT)
                os.mkdir(OUTPUT)
            except OSError:
                pass
        else:
            try:
                shutil.rmtree(os.path.join(OUTPUT, 'images'))
            except OSError:
                pass
        copytree(IMAGES, os.path.join(OUTPUT, 'images'))
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

    def generate_sitemap(self):
        '''
        Generates list of pages with titles.
        '''
        self.data['sitemap'] = []
        dbg('Generating sitemap:')
        for root, dirs, files in os.walk(TEMPLATES):
            if '.svn' in dirs:
                dirs.remove('.svn')  # don't visit .svn directories
            files.sort()
            dir = root[len(TEMPLATES):].strip('/')
            if len(dir) > 0:
                dir += '/'
            for file in files:
                name, ext = os.path.splitext(file)
                if name[:5] != 'PMASA' and ext != '.tpl':
                    continue
                if name[0] in ['_', '.']:
                    continue
                if file == 'index.xml.tpl':
                    continue
                dbg('- %s' % file)
                data = XML(open(os.path.join(root, file), 'r').read())
                title = str(data.select('def[@function="page_title"]/text()'))
                title = title.strip()
                if len(title) == 0:
                    title = str(data.select('def[@function="announcement_id"]/text()'))
                    title = title.strip()
                if len(title) == 0:
                    title = 'Index'
                self.data['sitemap'].append({
                    'link': dir + self.get_outname(name),
                    'title': title
                    })

    def get_translation_stats(self):
        '''
        Receives translation stats from external server and parses it.
        '''
        dbg('Processing translation stats...')
        try:
            lines = self.load_cache('translations')
        except NoCache:
            lines = urllib.urlopen(TRANSLATION_STATS_URL).readlines()
            self.save_cache('translations', lines)
        self.data['translations'] = []
        data = csv.reader(lines)
        for row in data:
            if row[4] != '':
                dt = fmtdate.parse(row[4][:10])
            else:
                dt = ''
            percent = float(row[3])
            if percent < 50:
                css = ' b50'
            elif percent < 80:
                css = ' b80'
            else:
                css =''
            self.data['translations'].append({
                'name': row[0],
                'short': row[1],
                'translated': row[2],
                'percent': row[3],
                'updated': dt,
                'css': css
            })

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

        self.get_translation_stats()

        self.list_security_issues()

        self.generate_sitemap()

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

        dbg('Generating CSS:')
        for css in [os.path.basename(x) for x in glob.glob('css/*.css')]:
            self.render_css(css)

        dbg('Generating JavaScript:')
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
