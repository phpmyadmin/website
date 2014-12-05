#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: set expandtab sw=4 ts=4 sts=4:
#
# phpMyAdmin web site generator
#
# Copyright (C) 2008 - 2013 Michal Cihar <michal@cihar.com>
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

import os
import re
import glob
import shutil
import datetime
import json
import ConfigParser
from xml.dom import DOMException
from genshi.template import TemplateLoader
from genshi.template import NewTextTemplate
from genshi.input import XML
from optparse import OptionParser
from dateutil.parser import parse
try:
    import tweepy
    TWITTER = True
except ImportError:
    TWITTER = False

import helper.cache
import helper.log
import helper.date
import helper.stringfmt

import data.awards
import data.themes
import data.menu
import data.screenshots
import data.redirects
import data.sf
import data.sitemap

# Filtering
FILES_REGEXP = re.compile(r'.*all-languages\.(zip).*')
BRANCH_REGEXP = re.compile(r'^([0-9]+\.[0-9]+)\.')
MAJOR_BRANCH_REGEXP = re.compile(r'^([0-9]+\.[0-9]+)\.')
LISTED_BRANCHES = set(('4.0', '4.1', '4.2', '4.3'))
TESTING_REGEXP = re.compile(r'.*(beta|alpha|rc).*')

# List of extensions allowed in downloads
DOWNLOAD_EXTS = ('.html', '.txt', '.7z', '.gz', '.bz2', '.xz', '.zip')

# Base URL (including trailing /)
SERVER = 'http://www.phpmyadmin.net'
BASE_URL = '/home_page/'
EXTENSION = 'php'

# How many security issues are shown in RSS
TOP_ISSUES = 10

# File locations
TEMPLATES = './templates'
CSS = './css'
JS = './js'
IMAGES = './images'
OUTPUT = './output'
STATIC = './static'

# Generic sourceforge.net part
PROJECT_FILES_RSS = \
    'http://sourceforge.net/api/file/index/project-id/23067/rss'
PROJECT_NEWS_RSS = \
    'https://sourceforge.net/p/phpmyadmin/news/feed'
PROJECT_VCS_RSS = \
    'http://github.com/phpmyadmin/phpmyadmin/commits/master.atom'
TRANSLATIONS_RSS = \
    'https://hosted.weblate.org/exports/rss/phpmyadmin/'
PLANET_RSS = \
    'http://planet.phpmyadmin.net/rss20.xml'
RSS_RU = \
    'http://php-myadmin.ru/rss/news.xml'

# Data sources
TRANSLATION_STATS = 'http://hosted.weblate.org/exports/stats/phpmyadmin/master/'

# URLS
SECURITY_URL = 'http://www.phpmyadmin.net/home_page/security/'

# Naming of versions
VERSION_INFO = (
    ('beta1', ' First beta version.'),
    ('beta2', ' Second beta version.'),
    ('beta3', ' Third beta version.'),
    ('beta4', ' Fourth beta version.'),
    ('beta', ' Beta version.'),
    ('rc1', ' First release candidate.'),
    ('rc2', ' Second release candidate.'),
    ('rc3', ' Third release candidate.'),
    ('rc4', ' Fourth release candidate.'),
    ('rc', ' Release candidate.'),
)


def fmt_bytes(number):
    '''
    Formats bytes to human readable form.
    '''
    number = int(number)
    if number > 10 * 1024 * 1024:
        return '%d MiB' % (number / (1024 * 1024))
    elif number > 1024 * 1024:
        return '%.1f MiB' % (number / (1024.0 * 1024))
    if number > 10 * 1024:
        return '%d KiB' % (number / 1024)
    elif number > 1024:
        return '%.1f KiB' % (number / 1024.0)
    else:
        return '%d bytes' % number


class SFGenerator(object):
    def __init__(self):
        self.data = {
            'releases': [],
            'releases_featured': [],
            'releases_older': [],
            'releases_beta': [],
            'themes': [],
            'news': [],
            'blogs': [],
            'issues': [],
            'base_url': BASE_URL,
            'server': SERVER,
            'file_ext': EXTENSION,
            'rss_files': PROJECT_FILES_RSS,
            'rss_translations': TRANSLATIONS_RSS,
            'rss_news': PROJECT_NEWS_RSS,
            'rss_planet': PLANET_RSS,
            'rss_security': '%s%ssecurity/index.xml' % (SERVER, BASE_URL),
            'rss_vcs': PROJECT_VCS_RSS,
            'screenshots': data.screenshots.SCREENSHOTS,
            'awards': data.awards.AWARDS,
            'generated': helper.date.DateTime.utcnow(),
            'themecssversions': data.themes.CSSVERSIONS,
            'sfservers': data.sf.SERVERS,
            'current_year': datetime.datetime.now().year,
        }
        self.loader = TemplateLoader([TEMPLATES])
        self.cssloader = TemplateLoader(
            [CSS],
            default_class=NewTextTemplate
        )
        self.staticloader = TemplateLoader(
            [STATIC],
            default_class=NewTextTemplate
        )
        self.jsloader = TemplateLoader(
            [JS],
            default_class=NewTextTemplate
        )
        self.feeds = helper.cache.FeedCache()
        self.xmls = helper.cache.XMLCache()
        self.urls = helper.cache.URLCache()

        # Load Twitter settings
        self.twitter = None
        if TWITTER:
            config = ConfigParser.RawConfigParser()
            config.read(os.path.expanduser('~/.pmaweb'))
            try:
                consumer_key = config.get('twitter', 'consumer_key')
                consumer_secret = config.get('twitter', 'consumer_secret')
                token_key = config.get('twitter', 'token_key')
                token_secret = config.get('twitter', 'token_secret')

                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(token_key, token_secret)

                self.twitter = tweepy.API(auth)
            except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
                pass

    def get_outname(self, page):
        '''
        Converts page name to file name. Basically only extension is appended
        if none is already used.
        '''
        if page.find('.') == -1:
            return '%s.%s' % (page, self.data['file_ext'])
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
        Converts text to something what can be used as a anchor or id (no
        spaces or other special chars).
        '''
        return re.sub('[^a-z0-9A-Z.-]', '_', text)

    def get_version_suffix(self, version):
        '''
        Returns suffix for a version.
        '''
        for match, result in VERSION_INFO:
            if version.find(match) != -1:
                return result
        return ''

    def get_version_info(self, version):
        '''
        Returns description to the phpMyAdmin version.
        '''
        if version[:2] == '1.':
            text = 'Historical release.'
        elif version[:2] == '2.':
            text = 'Version compatible with PHP 4+ and MySQL 3+.'
        elif version[:2] == '3.':
            text = (
                'Frames version not requiring Javascript. ' +
                'Requires PHP 5.2 and MySQL 5. ' +
                'Supported for security fixes only, until Jan 1, 2014.'
            )
        elif version[:3] == '4.4':
            text = 'Development version compatible with PHP 5.3 and MySQL 5.5.'
        elif version[:3] == '4.3':
            text = 'Current version compatible with PHP 5.3 and MySQL 5.5.'
        elif version[:3] == '4.2':
            text = 'Older version compatible with PHP 5.3 and MySQL 5.5.'
        elif version[:3] == '4.1':
            text = (
                'Older version compatible with PHP 5.3 and MySQL 5.5.' +
                'Supported for security fixes only, until Jan 1, 2015.'
            )
        elif version[:3] == '4.0':
            text = (
                'Older version compatible with PHP 5.2 and MySQL 5. ' +
                'Supported for security fixes only, until Jan 1, 2017.'
            )
        text += self.get_version_suffix(version)

        return text

    def dom2release(self, item, theme=False):
        '''
        Parses DOM object into release hash.
        '''
        title = item.getElementsByTagName('title')[0].childNodes[0].data
        helper.log.dbg('Processing release %s' % title)
        titleparts = title[1:].split('/')
        dltype = titleparts[0]
        version = titleparts[1]
        if theme:
            filename = titleparts[3]
        else:
            filename = titleparts[2]
        ext = os.path.splitext(filename)[1]
        link = item.getElementsByTagName('link')[0].childNodes[0].data
        pubdate = item.getElementsByTagName('pubDate')[0].childNodes[0].data
        featured = (FILES_REGEXP.match(filename) is not None)
        if featured:
            helper.log.dbg('Release is featured!')
        try:
            notes = item.getElementsByTagName(
                'files:release-notes-url'
            )[0].childNodes[0].data
        except (DOMException, IndexError):
            notes = ''
        media = item.getElementsByTagName('media:content')[0]
        size = media.getAttribute('filesize')
        for media_hash in media.getElementsByTagName('media:hash'):
            if media_hash.getAttribute('algo') == 'md5':
                md5 = media_hash.childNodes[0].data

        release = {
            'show': False,
            'version': version,
            'date': helper.date.DateTime.parse(pubdate[:-6] + ' GMT'),
            'name': dltype,
            'fullname': '%s %s' % (dltype, version),
            'notes': notes,
            'files': []
        }
        if not theme:
            release['info'] = self.get_version_info(version)

        file_info = {
            'name': filename,
            'url': link,
            'ext': ext,
            'featured': featured,
            'size': size,
            'size_k': int(size) / 1024,
            'size_m': int(size) / (1024 * 1024),
            'humansize': fmt_bytes(size),
            'md5': md5
        }

        return release, file_info

    def version_compare(self, first, second):
        '''
        Returns true if second version is newer than first one.
        '''
        # Check for identical versions
        if first == second:
            return False
        # Split out possible suffix like beta or rc
        first_parts = first.split('-')
        second_parts = second.split('-')

        # Extract numeric versions
        first = [int(x) for x in first_parts[0].split('.')]
        second = [int(x) for x in second_parts[0].split('.')]

        # Compare numbers
        if tuple(first) < tuple(second):
            return True
        if tuple(first) == tuple(second):
            # Second is final
            if len(second_parts) == 1:
                return True
            # First is final
            if len(first_parts) == 1:
                return False
            # Both are betas
            return (first_parts[1] < second_parts[1])

        return False

    def process_releases(self, xml_files):
        '''
        Gets phpMyAdmin releases out of releases feed and fills releases,
        releases_beta and releases_older.
        '''
        helper.log.dbg('Processing file releases...')
        releases_dict = {}
        for entry in xml_files.getElementsByTagName('item'):
            title = entry.getElementsByTagName('title')[0].childNodes[0].data
            titleparts = title[1:].split('/')
            if titleparts[0] != 'phpMyAdmin':
                continue
            dummy, ext = os.path.splitext(title)
            if ext not in DOWNLOAD_EXTS:
                continue
            release, file_info = self.dom2release(entry)
            if release is None:
                continue
            if release['version'] not in releases_dict:
                releases_dict[release['version']] = release
            if file_info['ext'] == '.html':
                releases_dict[release['version']]['notes'] = \
                    file_info['url'].replace('/download', '/view')
            else:
                releases_dict[release['version']]['files'].append(file_info)

        releases = [releases_dict[rel] for rel in releases_dict.keys()]

        helper.log.dbg('Sorting file lists...')
        releases.sort(key=lambda x: x['version'], reverse=True)

        helper.log.dbg('Detecting versions...')
        outversions = {}
        outbetaversions = {}

        # Split up versions to branches
        for idx in xrange(len(releases)):
            version = releases[idx]
            branch = BRANCH_REGEXP.match(version['version']).group(1)
            test = TESTING_REGEXP.match(version['version'])
            if test is not None:
                try:
                    if self.version_compare(
                            releases[outbetaversions[branch]]['version'],
                            version['version']):
                        outbetaversions[branch] = idx
                except KeyError:
                    outbetaversions[branch] = idx
            else:
                try:
                    if self.version_compare(
                            releases[outversions[branch]]['version'],
                            version['version']):
                        outversions[branch] = idx
                except KeyError:
                    outversions[branch] = idx

        # Check for old beta versions
        for beta in outbetaversions.keys():
            try:
                stable_rel = releases[outversions[beta]]['version']
                beta_rel = releases[outbetaversions[beta]]['version'].split(
                    '-'
                )[0]
                if stable_rel > beta_rel or stable_rel == beta_rel:
                    helper.log.dbg(
                        'Old beta: %s' %
                        releases[outbetaversions[beta]]['version']
                    )
                    del outbetaversions[beta]
            except KeyError:
                pass

        # Check for old stable releases
        for stable in outversions.keys():
            version = releases[outversions[stable]]['version']
            major_branch = MAJOR_BRANCH_REGEXP.match(version).group(1)
            if major_branch not in LISTED_BRANCHES:
                del outversions[stable]
                continue
            for check in outversions.keys():
                try:
                    check_version = releases[outversions[check]]['version']
                except KeyError:
                    # We already marked this one as old
                    continue
                if (major_branch == check_version[:len(major_branch)]
                        and self.version_compare(version, check_version)):
                    helper.log.dbg('Old release: %s' % version)
                    del outversions[stable]
                    continue

        featured = max(outversions.keys())
        featured_id = outversions[featured]

        helper.log.dbg('Versions detected:')
        for idx in xrange(len(releases)):
            if idx in outversions.values():
                self.data['releases'].append(releases[idx])
                if featured_id == idx:
                    releases[idx]['info'] += ' Currently recommended version.'
                    self.data['releases_featured'].append(releases[idx])
                    helper.log.dbg(' %s (featured)' % releases[idx]['version'])
                else:
                    helper.log.dbg(' %s' % releases[idx]['version'])
            elif idx in outbetaversions.values():
                self.data['releases_beta'].append(releases[idx])
                helper.log.dbg(' %s (beta)' % releases[idx]['version'])
            else:
                self.data['releases_older'].append(releases[idx])
                helper.log.dbg(' %s (old)' % releases[idx]['version'])

    def process_themes(self, xml_files):
        '''
        Gets theme releases out of releases feed and fills themes.
        '''
        helper.log.dbg('Processing themes releases...')
        for entry in xml_files.getElementsByTagName('item'):
            title = entry.getElementsByTagName('title')[0].childNodes[0].data
            titleparts = title[1:].split('/')
            if titleparts[0] != 'themes':
                continue
            dummy, ext = os.path.splitext(title)
            if ext not in DOWNLOAD_EXTS:
                continue
            name = titleparts[1]
            version = titleparts[2]
            release, file_info = self.dom2release(entry, theme=True)
            if release is None:
                continue
            release['shortname'] = name
            release['ignore'] = False
            release['imgname'] = 'images/themes/%s.png' % name
            try:
                release.update(data.themes.THEMES['%s-%s' % (name, version)])
            except KeyError:
                helper.log.warn(
                    'No metadata for theme %s-%s!' % (name, version)
                )
                release['name'] = name
                release['support'] = 'N/A'
                release['info'] = ''
            release['fullname'] = '%s %s' % (release['name'], version)
            release['classes'] = data.themes.CSSMAP[release['support']]

            release['file'] = file_info
            if not release['ignore']:
                self.data['themes'].append(release)

        helper.log.dbg('Sorting file lists...')
        self.data['themes'].sort(key=lambda x: x['date'], reverse=True)

    def process_news(self, feed):
        '''
        Fills in news based on news feed.
        '''
        helper.log.dbg('Processing news feed...')
        for entry in feed.entries:
            item = {}
            item['link'] = entry.link
            item['date'] = helper.date.DateTime.parse(entry.updated)
            # replaces are workaround for broken automatic links from sf.net
            # rss feed
            item['text'] = entry.summary.replace(
                '.</a>', '</a>.'
            ).replace(
                '.">http', '">http'
            )
            item['title'] = entry.title
            item['anchor'] = self.text_to_id(entry.title)
            self.data['news'].append(item)

        self.data['short_news'] = self.data['news'][:5]

    def tweet(self):
        '''
        Finds out whether we should send update to twitter and do so.
        '''
        if self.twitter is None:
            return
        news = self.data['news'][0]

        storage = helper.cache.Cache()
        title = news['title']
        if 'phpMyAdmin' in news['title']:
            title = title.replace('phpMyAdmin', '#phpMyAdmin')
        else:
            title = '%s #phpMyAdmin' % title
        tweet = '%s, see http://www.phpmyadmin.net/' % title
        try:
            last = storage.force_get('last-tweet')
        except helper.cache.NoCache:
            last = None
        if last == tweet:
            helper.log.dbg(
                'No need to tweet, the last news is still the same...'
            )
            return
        helper.log.dbg('Tweeting: %s' % tweet)
        self.twitter.update_status(tweet)
        storage.set('last-tweet', tweet)

    def tweet_security(self):
        '''
        Finds out whether we should send update to twitter about
        security issue and do so.
        '''
        if self.twitter is None:
            return
        issue = self.data['issues'][0]
        storage = helper.cache.Cache()
        tweet = '%s: %s - %s #security' % (
            issue['name'],
            issue['summary'].strip(),
            issue['fulllink'],
        )
        try:
            last = storage.force_get('last-security-tweet')
        except helper.cache.NoCache:
            last = None
        if last == tweet:
            helper.log.dbg(
                'No need to tweet, the last news is still the same...'
            )
            return
        helper.log.dbg('Tweeting: %s' % tweet)
        self.twitter.update_status(tweet)
        storage.set('last-security-tweet', tweet)

    def process_planet(self, feed):
        '''
        Fills in planet based on planet feed.
        '''
        helper.log.dbg('Processing planet feed...')
        for entry in feed.entries:
            item = {}
            item['link'] = 'http://planet.phpmyadmin.net/#%s' % entry.link
            item['date'] = helper.date.DateTime.parse(
                entry.updated.replace('+0000', 'GMT')
            )
            if hasattr(entry, 'summary_detail'):
                item['text'] = entry.summary_detail['value']
            else:
                item['text'] = ''
            item['title'] = entry.title
            self.data['blogs'].append(item)

        self.data['short_blogs'] = self.data['blogs'][:5]

    def process_feed(self, name, feed, count=3):
        '''
        Fills in feed data based on feeparser feed.
        '''
        helper.log.dbg('Processing %s feed...' % name)
        self.data[name] = []
        for entry in feed.entries:
            item = {}
            item['link'] = entry.link
            item['date'] = entry.updated_parsed
            item['text'] = entry.summary_detail['value']
            item['title'] = entry.title
            self.data[name].append(item)

        self.data['short_%s' % name] = self.data[name][:count]

    def get_menu(self, active):
        '''
        Returns list of menu entries with marked active one.
        '''
        menu = []
        for item in data.menu.MENU:
            title = item[1]
            name = item[0]
            field = {
                'title': title,
                'class': {},
            }
            if name == active or '%sindex' % name == active:
                field['class'] = {
                    'class': 'active',
                }
            if len(name) > 0 and name[-1] != '/':
                name = self.get_outname(name)
            field['link'] = '%s%s' % (BASE_URL, name)
            menu.append(field)
        return menu

    def render_css(self, filename):
        '''
        Renders CSS file from template.
        '''
        helper.log.dbg('  %s' % filename)
        template = self.cssloader.load(filename)
        with open(os.path.join(OUTPUT, 'css', filename), 'w') as out:
            out.write(template.generate(**self.data).render(encoding='utf-8'))

    def render_static(self, templatename, outfile, extradata=None):
        '''
        Renders "static" file from template.
        '''
        if extradata is None:
            extradata = {}
        helper.log.dbg('  %s' % outfile)
        template = self.staticloader.load(templatename)
        with open(os.path.join(OUTPUT, outfile), 'w') as out:
            extradata.update(self.data)
            out.write(template.generate(**extradata).render(encoding='utf-8'))

    def render_js(self, filename):
        '''
        Renders JavaScript file from template. Some defined files are not
        processed through template engine as they were taken from other
        projects.
        '''
        helper.log.dbg('  %s' % filename)
        outpath = os.path.join(OUTPUT, 'js', filename)
        shutil.copy2(os.path.join(JS, filename), outpath)

    def render(self, page):
        '''
        Renders standard page.
        '''
        helper.log.dbg('  %s' % page)
        template = self.loader.load('%s.tpl' % page)
        menu = self.get_menu(page)
        with open(os.path.join(OUTPUT, self.get_outname(page)), 'w') as out:
            out.write(
                template.generate(menu=menu, **self.data).render(
                    self.get_renderer(page),
                    encoding='utf-8'
                )
            )

    def render_security(self, issue):
        '''
        Renders security issue.
        '''
        helper.log.dbg('  %s' % issue)
        template = self.loader.load('security/%s' % issue)
        menu = self.get_menu('security/')
        filename = os.path.join(
            OUTPUT,
            'security',
            self.get_outname(issue)
        )
        with open(filename, 'w') as out:
            out.write(
                template.generate(menu=menu, issue=issue, **self.data).render(
                    'xhtml',
                    encoding='utf-8'
                )
            )

    def list_security_issues(self):
        '''
        Fills in issues and topissues with security issues information.
        '''
        issues = glob.glob('templates/security/PMASA-*')
        issues.sort(key=lambda x: int(x[24:29]) * 100 - int(x[30:]))
        for issue in issues:
            xmldata = XML(open(issue, 'r').read())
            name = os.path.basename(issue)
            self.data['issues'].append({
                'name': name,
                'link': '%ssecurity/%s' % (BASE_URL, self.get_outname(name)),
                'fulllink': '%s%ssecurity/%s' % (
                    SERVER, BASE_URL, self.get_outname(name)
                ),
                'summary': str(xmldata.select(
                    'def[@function="announcement_summary"]/text()'
                )),
                'date': helper.date.DateTime.parse(str(xmldata.select(
                    'def[@function="announcement_date"]/text()'
                ))),
                'cves': str(xmldata.select(
                    'def[@function="announcement_cve"]/text()'
                )).split(' '),
                'versions': str(xmldata.select(
                    'def[@function="announcement_affected"]/text()'
                )),
            })
        self.data['topissues'] = self.data['issues'][:TOP_ISSUES]

    def prepare_output(self):
        '''
        Copies static content to output and creates required directories.
        '''
        helper.log.dbg('Copying static content to output...')
        try:
            shutil.rmtree(OUTPUT)
        except OSError:
            pass
        copyignore = shutil.ignore_patterns('.git', '.svn', '*.swp', '_*')
        shutil.copytree(STATIC, OUTPUT, ignore=copyignore)
        imgdst = os.path.join(OUTPUT, 'images')
        shutil.copytree(IMAGES, imgdst, ignore=copyignore)
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

    def get_sitemap_data(self, page):
        '''
        Returns metadata for page for sitemap as per http://sitemaps.org.
        '''
        priority = '0.8'
        changefreq = 'daily'
        if page[:15] == 'security/PMASA-':
            priority = '0.5'
            changefreq = 'monthly'
        elif page[:20] == '/pma_localized_docs/':
            priority = '0.6'
            changefreq = 'monthly'
        elif page in ['index', 'news']:
            priority = '1.0'
            changefreq = 'daily'
        elif page in ['improve', 'team', 'docs', 'devel', 'translate']:
            priority = '1.0'
            changefreq = 'weekly'
        elif page in ['downloads', 'donate', 'themes', 'translations']:
            priority = '0.9'
            changefreq = 'daily'
        elif page in ['support']:
            priority = '0.9'
            changefreq = 'weekly'
        elif page in ['sitemap']:
            priority = '0.2'
            changefreq = 'weekly'
        return {
            'lastmod': helper.date.DateTime.utcnow(),
            'changefreq': changefreq,
            'priority': priority,
        }

    def generate_sitemap(self):
        '''
        Generates list of pages with titles.
        '''
        self.data['sitemap'] = []
        self.data['sitemapxml'] = []
        helper.log.dbg('Generating sitemap:')
        for root, dirs, files in os.walk(TEMPLATES):
            if '.svn' in dirs:
                dirs.remove('.svn')  # don't visit .svn directories
            if '.git' in dirs:
                dirs.remove('.git')  # don't visit .git directories
            files.sort()
            root_dir = root[len(TEMPLATES):].strip('/')
            if len(root_dir) > 0:
                root_dir += '/'
            for filename in files:
                name, ext = os.path.splitext(filename)
                if ext != '.tpl' and name[:6] != 'PMASA-':
                    continue
                if name[0] in ['_', '.']:
                    continue
                if filename in ['index.xml.tpl', 'sitemap.xml.tpl', '404.tpl']:
                    continue
                helper.log.dbg('- %s' % filename)
                xmldata = XML(open(os.path.join(root, filename), 'r').read())
                title = str(xmldata.select(
                    'def[@function="page_title"]/text()'
                ))
                title = title.strip()
                if len(title) == 0:
                    title = str(xmldata.select(
                        'def[@function="announcement_id"]/text()'
                    ))
                    title = title.strip()
                if len(title) == 0:
                    title = 'Index'
                link = root_dir + self.get_outname(name)
                sitemap = {
                    'link': link,
                    'loc': '%s%s%s' % (SERVER, BASE_URL, link),
                    'title': title
                }
                if name[:6] != 'PMASA-':
                    self.data['sitemap'].append(sitemap)
                sitemap.update(self.get_sitemap_data(root_dir + name))
                self.data['sitemapxml'].append(sitemap)
        for link in data.sitemap.ENTRIES:
            sitemap = {
                'loc': SERVER + link,
            }
            sitemap.update(self.get_sitemap_data(link))
            self.data['sitemapxml'].append(sitemap)

    def get_translation_stats(self):
        '''
        Receives translation stats from external server and parses it.
        '''
        helper.log.dbg('Processing translation stats...')
        self.data['translations'] = []
        stats = json.loads(self.urls.load('translations', TRANSLATION_STATS))

        for lang in stats:
            if lang['translated_percent'] < 50:
                css = ' b50'
            elif lang['translated_percent'] < 80:
                css = ' b80'
            else:
                css = ''
            if lang['last_change'] is None:
                updated = ''
            else:
                updated = parse(lang['last_change'])
            translation = {
                'name': lang['name'],
                'short': lang['code'],
                'url': lang['url'],
                'translated': lang['translated'],
                'percent': lang['translated_percent'],
                'updated': updated,
                'css': css,
            }
            self.data['translations'].append(translation)

    def fetch_data(self):
        '''
        Fetches data from remote or local sources and prepares template data.
        '''
        xml_files = self.xmls.load('files', PROJECT_FILES_RSS)

        self.process_releases(xml_files)
        self.process_themes(xml_files)

        rss_news = self.feeds.load('news', PROJECT_NEWS_RSS)
        self.process_news(rss_news)

        self.tweet()

        rss_planet = self.feeds.load('planet', PLANET_RSS)
        self.process_planet(rss_planet)

        rss_ru = self.feeds.load('ru', RSS_RU)
        self.process_feed('news_ru', rss_ru)

        self.get_translation_stats()

        self.list_security_issues()

        self.tweet_security()

        self.generate_sitemap()

    def render_pages(self):
        '''
        Renders all content pages.
        '''
        helper.log.dbg('Rendering pages:')
        templates = [os.path.basename(x) for x in glob.glob('templates/*.tpl')]
        templates.extend(
            [
                os.path.join('security', os.path.basename(x))
                for x in glob.glob('templates/security/*.tpl')
            ]
        )
        for template in templates:
            name = os.path.splitext(template)[0]
            if os.path.basename(name)[0] == '_':
                continue
            self.render(name)

        helper.log.dbg('Rendering security issues pages:')
        for issue in self.data['issues']:
            self.render_security(issue['name'])

        helper.log.dbg('Generating CSS:')
        for cssfile in glob.glob('css/*.css'):
            self.render_css(os.path.basename(cssfile))

        helper.log.dbg('Generating JavaScript:')
        for jsfile in glob.glob('js/*.js'):
            self.render_js(os.path.basename(jsfile))

        helper.log.dbg('Generating static pages:')
        self.render_static('_version.php', 'version.php')
        self.render_static('_version.txt', 'version.txt')
        self.render_static('_version.js', 'version.js')
        self.render_static('_version.json', 'version.json')
        self.render_static('_security.php', 'security.php')
        self.render_static('_robots.txt', 'robots.txt')
        for redir in data.redirects.REDIRECTS:
            self.render_static(
                '_redirect.tpl',
                '%s.php' % redir,
                {'location': self.get_outname(data.redirects.REDIRECTS[redir])}
            )

    def main(self):
        '''
        Main program which does everything.
        '''
        self.prepare_output()
        self.fetch_data()
        self.render_pages()
        helper.log.dbg('Done!')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option(
        '-v', '--verbose',
        action='store_true',
        dest='verbose',
        help='Output verbose information.'
    )
    parser.add_option(
        '-q', '--quiet',
        action='store_false',
        dest='verbose',
        help='Only show errors and warnings.'
    )
    parser.add_option(
        '-V', '--verbose-cache',
        action='store_true',
        dest='verbose_cache',
        help='Output verbose caching information.'
    )
    parser.add_option(
        '-Q', '--quiet-cache',
        action='store_false',
        dest='verbose_cache',
        help='No information from caching in output.'
    )
    parser.add_option(
        '-s', '--server',
        action='store', type='string',
        dest='server',
        help='Name of server where data will be published, eg.: %s.' % SERVER
    )
    parser.add_option(
        '-b', '--base-url',
        action='store', type='string',
        dest='base_url',
        help='Base URL of document, eg.: %s.' % BASE_URL
    )
    parser.add_option(
        '-e', '--extension',
        action='store', type='string',
        dest='extension',
        help='Extension of generated files, default is %s.' % EXTENSION
    )
    parser.add_option(
        '-l', '--log',
        action='store', type='string',
        dest='log',
        help='Log filename, default is none.'
    )

    parser.set_defaults(
        verbose=helper.log.VERBOSE,
        verbose_cache=helper.log.DBG_CACHE,
        server=SERVER,
        base_url=BASE_URL,
        log=None,
        extension=EXTENSION,
    )

    (options, args) = parser.parse_args()

    helper.log.VERBOSE = options.verbose
    helper.log.DBG_CACHE = options.verbose_cache
    SERVER = options.server
    BASE_URL = options.base_url
    EXTENSION = options.extension
    if options.log is not None:
        helper.log.LOG = open(options.log, 'w')

    gen = SFGenerator()
    gen.main()
