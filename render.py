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
import re
import glob
import shutil
import csv
import traceback
import datetime
import polib
from genshi.template import TemplateLoader
from genshi.template import NewTextTemplate
from genshi.input import XML
from optparse import OptionParser

import helper.cache
import helper.log
import helper.date
import helper.stringfmt
import helper.twitter

import data.awards
import data.themes
import data.langnames
import data.menu
import data.screenshots
import data.redirects
import data.sf
import data.sitemap

# Project part
PROJECT_ID = 23067
PROJECT_NAME = 'phpmyadmin'

# Filtering
FILES_REGEXP = re.compile(r'.*all-languages\.(zip|tar\.gz).*')
BRANCH_REGEXP = re.compile('^([0-9]+\.[0-9]+)\.')
MAJOR_BRANCH_REGEXP = re.compile('^([0-9]+)\.')
TESTING_REGEXP = re.compile('.*(beta|alpha|rc).*')
SIZE_REGEXP = re.compile('.*\(([0-9]+) bytes, ([0-9]+) downloads to date')
LANG_REGEXP ='((translation|lang|%s)\W.*update|update.*\W(translation|lang|%s)($|\W)|^updated?$|new lang|better word|fix.*translation($|\W)|Translation update done using Pootle)'

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

# Which JS files are not templates
JS_TEMPLATES = []

# Generic sourceforge.net part
PROJECT_FILES_RSS = 'https://sourceforge.net/export/rss2_projfiles.php?group_id=%d&rss_limit=100' % PROJECT_ID
PROJECT_FILES_RSS = 'https://sourceforge.net/api/file/index/project-id/%d/rss' % PROJECT_ID
PROJECT_NEWS_RSS = 'https://sourceforge.net/export/rss2_projnews.php?group_id=%d&rss_fulltext=1&limit=10' % PROJECT_ID
PROJECT_SUMMARY_RSS = 'https://sourceforge.net/export/rss2_projsummary.php?group_id=%d' % PROJECT_ID
DONATIONS_RSS = 'https://sourceforge.net/export/rss2_projdonors.php?group_id=%d&limit=20' % PROJECT_ID
PROJECT_VCS_RSS = 'http://cia.vc/stats/project/phpmyadmin/.rss'
PROJECT_DL = 'http://prdownloads.sourceforge.net/%s/%%s' % PROJECT_NAME
PROJECT_GIT = 'git://phpmyadmin.git.sourceforge.net/gitroot/phpmyadmin/phpmyadmin'
PLANET_RSS = 'http://planet.phpmyadmin.net/rss20.xml'
RSS_CZ = 'http://phpmyadmin.cz/rss.xml'
RSS_RU = 'http://php-myadmin.ru/rss/news.xml'

# Data sources
SNAPSHOT_MD5 = 'http://dl.cihar.com/phpMyAdmin/master/md5.sums'
SNAPSHOT_SIZES = 'http://dl.cihar.com/phpMyAdmin/master/files.list'

# Clean output before generating
CLEAN_OUTPUT = True

# RSS parsing
SUMMARY_DEVS = re.compile('Developers on project: ([0-9]*)')
SUMMARY_ACTIVITY = re.compile('Activity percentile \(last week\): ([0-9.]*%)')
SUMMARY_DOWNLOADS = re.compile('Downloadable files: ([0-9]*) total downloads to date')
SUMMARY_LISTS = re.compile('Mailing lists \(public\): ([0-9]*)')
SUMMARY_FORUMS = re.compile('Discussion forums \(public\): ([0-9]*), containing ([0-9]*) messages')
SUMMARY_TRACKER = re.compile('Tracker: (.*) \(([0-9]*) open/([0-9]*) total\)')

# Indenti.ca integration
IDENTICA_USER = 'phpmyadmin'
IDENTICA_PASSWORD = None

def copytree(src, dst):
    '''
    Trimmed down version of shutil.copytree. Recursively copies a directory
    tree using shutil.copy2().

    The destination directory must not already exist.
    If exception(s) occur, an Error is raised with a list of reasons.

    It handles only files and dirs and ignores .svn and *.swp* files and
    files starting with underscore (_).
    '''
    names = os.listdir(src)
    errors = []
    for name in names:
        if name == '.git' or name == '.svn' or name.find('.swp') != -1 or name[0] == '_':
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.isdir(srcname):
                os.makedirs(dstname)
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

def fmt_bytes(number):
    '''
    Formats bytes to human readable form.
    '''
    number = int(number)
    if number > 10 * 1024 * 1024:
        return '%d MiB' % (number / ( 1024 * 1024 ))
    elif number > 1024 * 1024:
        return '%.1f MiB' % (number / ( 1024.0 * 1024 ))
    if number > 10 * 1024:
        return '%d KiB' % (number / 1024 )
    elif number > 1024:
        return '%.1f KiB' % (number / 1024.0 )
    else:
        return '%d bytes' % number

class SFGenerator:
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
            'donations': [],
            'base_url': BASE_URL,
            'server': SERVER,
            'file_ext': EXTENSION,
            'rss_files': PROJECT_FILES_RSS,
            'rss_donations': DONATIONS_RSS,
            'rss_news': PROJECT_NEWS_RSS,
            'rss_planet': PLANET_RSS,
            'rss_summary': PROJECT_SUMMARY_RSS,
            'rss_security': '%s%ssecurity/index.xml' % (SERVER, BASE_URL),
            'rss_vcs': PROJECT_VCS_RSS,
            'screenshots': data.screenshots.SCREENSHOTS,
            'awards': data.awards.AWARDS,
            'generated': helper.date.fmtdatetime.utcnow(),
            'themecssversions': data.themes.CSSVERSIONS,
            'sfservers': data.sf.SERVERS,
            'current_year': datetime.datetime.now().year,
            }
        self.loader = TemplateLoader([TEMPLATES])
        self.cssloader = TemplateLoader([CSS], default_class = NewTextTemplate)
        self.staticloader = TemplateLoader([STATIC], default_class = NewTextTemplate)
        self.jsloader = TemplateLoader([JS], default_class = NewTextTemplate)
        self.feeds = helper.cache.FeedCache()
        self.xmls = helper.cache.XMLCache()
        self.urls = helper.cache.URLCache()
        self.git = helper.cache.GitCache(PROJECT_GIT)

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
        Converts text to something what can be used as a anchor or id (no spaces
        or other special chars).
        '''
        return re.sub('[^a-z0-9A-Z.-]', '_', text)

    def get_version_info(self, version):
        '''
        Returns description to the phpMyAdmin version.
        '''
        if version[:2] == '2.':
            text ='Version compatible with PHP 4+ and MySQL 3+.'
        elif version[:2] == '3.':
            text = 'Version compatible with PHP 5 and MySQL 5.'
        if version.find('beta1') != -1:
            text += ' First beta version.'
        elif version.find('beta2') != -1:
            text += ' Second beta version.'
        elif version.find('beta') != -1:
            helper.log.warn('Generic beta: %s' % version)
            text += ' Beta version.'
        elif version.find('rc1') != -1:
            text += ' First release candidate.'
        elif version.find('rc2') != -1:
            text += ' Second release candidate.'
        elif version.find('rc3') != -1:
            text += ' Third release candidate.'
        elif version.find('rc') != -1:
            text += ' Release candidate.'
            helper.log.warn('Generic RC: %s' % version)

        return text

    def dom2release(self, item, theme = False):
        '''
        Parses DOM object into release hash.

        Basically it gets XML like this:

      <title><![CDATA[/theme-xampp/2.11/xampp-2.11.zip]]></title>
        <item>
          <title><![CDATA[/phpMyAdmin/3.2.1/phpMyAdmin-3.2.1-all-languages.tar.gz]]></title>
          <link>http://sourceforge.net/projects/phpmyadmin/files/phpMyAdmin/3.2.1/phpMyAdmin-3.2.1-all-languages.tar.gz/download</link>
          <guid>http://sourceforge.net/projects/phpmyadmin/files/phpMyAdmin/3.2.1/phpMyAdmin-3.2.1-all-languages.tar.gz/download</guid>
          <description><![CDATA[/phpMyAdmin/3.2.1/phpMyAdmin-3.2.1-all-languages.tar.gz]]></description>
          <pubDate>Sun, 09 Aug 2009 21:27:17 +0000</pubDate>
          <files:extra-info xmlns:files="http://sourceforge.net/api/files.rdf#">HTML document text</files:extra-info>
          <media:content xmlns:media="http://video.search.yahoo.com/mrss/" type="text/html" url="http://sourceforge.net/project/phpmyadmin/files/phpMyAdmin/3.2.1/phpMyAdmin-3.2.1-notes.html/download" filesize="1539"><media:title></media:title><media:hash algo="md5">b9e4de4108f1d6e5fc4772df888e73ac</media:hash></media:content>
          <files:download-count xmlns:files="http://sourceforge.net/api/files.rdf#">0</files:download-count>
        </item>
        '''
        title = item.getElementsByTagName('title')[0].childNodes[0].data
        helper.log.dbg('Processing release %s' % title)
        titleparts = title[1:].split('/')
        type = titleparts[0]
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
        dlcount = item.getElementsByTagName('files:download-count')[0].childNodes[0].data
        try:
            notes = item.getElementsByTagName('files:release-notes-url')[0].childNodes[0].data
        except:
            notes = ''
        media = item.getElementsByTagName('media:content')[0]
        size = media.getAttribute('filesize')
        for hash in media.getElementsByTagName('media:hash'):
            if hash.getAttribute('algo') == 'md5':
                md5 = hash.childNodes[0].data

        release = {
            'show': False,
            'version': version,
            'date': helper.date.fmtdatetime.parse(pubdate[:-6] + ' GMT'),
            'name': type,
            'fullname': '%s %s' % (type, version),
            'notes': notes,
            'files': []
        }
        if not theme:
            release['info'] = self.get_version_info(version)

        file = {
            'name': filename,
            'url': link,
            'ext': ext,
            'featured': featured,
            'size': size,
            'size_k' : int(size) / 1024,
            'size_m' : int(size) / (1024 * 1024),
            'humansize': fmt_bytes(size),
            'dlcount': dlcount,
            'md5': md5}

        return release, file

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
        f = [int(x) for x in first_parts[0].split('.')]
        s = [int(x) for x in second_parts[0].split('.')]

        # Compare numbers
        if tuple(f) < tuple(s):
            return True
        if tuple(f) == tuple(s):
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
            type = titleparts[0]
            if type != 'phpMyAdmin':
                continue
            path, ext = os.path.splitext(title)
            if ext not in ['.html', '.txt', '.7z', '.gz', '.bz2', '.xz', '.zip']:
                continue
            release, file = self.dom2release(entry)
            if release is None:
                continue
            if not releases_dict.has_key(release['version']):
                releases_dict[release['version']] = release
            if file['ext'] == '.html':
                releases_dict[release['version']]['notes'] = file['url'].replace('/download', '/view')
            else:
                releases_dict[release['version']]['files'].append(file)

        releases = [releases_dict[rel] for rel in releases_dict.keys()]

        helper.log.dbg('Sorting file lists...')
        releases.sort(key = lambda x: x['version'], reverse = True)

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
                    if self.version_compare(releases[outbetaversions[branch]]['version'], version['version']):
                        outbetaversions[branch] = idx
                except KeyError:
                    outbetaversions[branch] = idx
            else:
                try:
                    if self.version_compare(releases[outversions[branch]]['version'], version['version']):
                        outversions[branch] = idx
                except KeyError:
                    outversions[branch] = idx

        # Check for old beta versions
        for beta in outbetaversions.keys():
            try:
                stable_rel = releases[outversions[beta]]['version']
                beta_rel = releases[outbetaversions[beta]]['version'].split('-')[0]
                if stable_rel > beta_rel or stable_rel == beta_rel:
                    helper.log.dbg('Old beta: %s' % releases[outbetaversions[beta]]['version'])
                    del outbetaversions[beta]
            except KeyError:
                pass

        # Check for old stable releases
        for stable in outversions.keys():
            version = releases[outversions[stable]]['version']
            major_branch = MAJOR_BRANCH_REGEXP.match(version).group(1)
            for check in outversions.keys():
                try:
                    check_version = releases[outversions[check]]['version']
                except KeyError:
                    # We already marked this one as old
                    continue
                if major_branch == check_version[:len(major_branch)] and self.version_compare(version, check_version):
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

    def get_snapshots_info(self):
        '''
        Retrieves vcs snapshots info and fills it in data['release_vcs'].
        '''
        md5_strings = self.urls.load(SNAPSHOT_MD5).split('\n')
        size_strings = self.urls.load(SNAPSHOT_SIZES).split('\n')
        md5s = {}
        for line in md5_strings:
            if line.strip() == '':
                continue
            md5, name = line.split('  ')
            md5s[name] = md5
        vcs = []
        for line in size_strings:
            if line.strip() == '':
                continue
            name, size = line.split(' ')
            vcs.append({
                'name' : name,
                'size' : int(size),
                'size_k' : int(size) / 1024,
                'size_m' : int(size) / (1024 * 1024),
                'humansize' : fmt_bytes(size),
                'url' : 'http://dl.cihar.com/phpMyAdmin/master/%s' % name,
                'md5' : md5s[name],
            })
        self.data['release_vcs'] = vcs

    def process_themes(self, xml_files):
        '''
        Gets theme releases out of releases feed and fills themes.
        '''
        helper.log.dbg('Processing themes releases...')
        for entry in xml_files.getElementsByTagName('item'):
            title = entry.getElementsByTagName('title')[0].childNodes[0].data
            titleparts = title[1:].split('/')
            type = titleparts[0]
            if type != 'themes':
                continue
            path, ext = os.path.splitext(title)
            if ext not in ['.html', '.txt', '.7z', '.gz', '.bz2', '.xz', '.zip']:
                continue
            name = titleparts[1]
            version = titleparts[2]
            release, file = self.dom2release(entry, theme = True)
            if release is None:
                continue
            release['shortname'] = name
            release['ignore'] = False
            release['imgname'] = 'images/themes/%s.png' % name
            try:
                release.update(data.themes.THEMES['%s-%s' % (name, version)])
            except KeyError:
                helper.log.warn('No meatadata for theme %s-%s!' % (name, version))
                release['name'] = name
                release['support'] = 'N/A'
                release['info'] = ''
            release['fullname'] = '%s %s' % (release['name'], version)
            release['classes'] = data.themes.CSSMAP[release['support']]

            release['file'] = file
            if not release['ignore']:
                self.data['themes'].append(release)

        helper.log.dbg('Sorting file lists...')
        self.data['themes'].sort(key = lambda x: x['date'], reverse = True)

    def process_news(self, feed):
        '''
        Fills in news based on news feed.
        '''
        helper.log.dbg('Processing news feed...')
        for entry in feed.entries:
            item = {}
            item['link'] = entry.link
            item['date'] = helper.date.fmtdatetime.parse(entry.updated)
            # replaces are workaround for broken automatic links from sf.net rss feed
            item['text'] = entry.summary.replace('.</a>', '</a>.').replace('.">http', '">http')
            item['comments_link'] = entry.comments
            item['comments_number'] = 0
            item['title'] = entry.title
            item['anchor'] = self.text_to_id(entry.title)
            self.data['news'].append(item)

        self.data['short_news'] = self.data['news'][:5]

    def tweet(self):
        '''
        Finds out whether we should send update to identi.ca and twitter and do so.
        '''
        news = self.data['news'][0]
        if IDENTICA_USER is None or IDENTICA_PASSWORD is None:
            return
        storage = helper.cache.Cache()
        tweet = '%s | http://www.phpmyadmin.net/ | #phpmyadmin' % news['title']
        try:
            last = storage.force_get('last-tweet')
        except helper.cache.NoCache:
            last = None
        if last == tweet:
            helper.log.dbg('No need to tweet, the last news is still the same...')
            return
        helper.log.dbg('Tweeting to identi.ca: %s' % tweet)
        api = helper.twitter.Api(username = IDENTICA_USER,
                password = IDENTICA_PASSWORD,
                twitterserver='identi.ca/api')
        api.SetSource('phpMyAdmin website')
        api.PostUpdate(tweet)
        storage.set('last-tweet', tweet)

    def tweet_security(self):
        '''
        Finds out whether we should send update to identi.ca and twitter about
        security issue and do so.
        '''
        issue = self.data['issues'][0]
        if IDENTICA_USER is None or IDENTICA_PASSWORD is None:
            return
        storage = helper.cache.Cache()
        tweet = '%s | http://www.phpmyadmin.net/home_page/security/ | #phpmyadmin #pmasa #security' % issue['name']
        try:
            last = storage.force_get('last-security-tweet')
        except helper.cache.NoCache:
            last = None
        if last == tweet:
            helper.log.dbg('No need to tweet, the last news is still the same...')
            return
        helper.log.dbg('Tweeting to identi.ca: %s' % tweet)
        api = helper.twitter.Api(username = IDENTICA_USER,
                password = IDENTICA_PASSWORD,
                twitterserver='identi.ca/api')
        api.SetSource('phpMyAdmin website')
        api.PostUpdate(tweet)
        storage.set('last-security-tweet', tweet)

    def process_planet(self, feed):
        '''
        Fills in planet based on planet feed.
        '''
        helper.log.dbg('Processing planet feed...')
        for entry in feed.entries:
            item = {}
            item['link'] = 'http://planet.phpmyadmin.net/#%s' % entry.link
            item['date'] = helper.date.fmtdatetime.parse(entry.updated.replace('+0000', 'GMT'))
            item['text'] = entry.summary_detail['value']
            item['title'] = entry.title
            self.data['blogs'].append(item)

        self.data['short_blogs'] = self.data['blogs'][:5]

    def process_feed(self, name, feed, count = 3):
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

        self.data['short_%s' % name ] = self.data[name][:count]

    def process_donations(self, feed):
        '''
        Fills in donations based on donations feed.
        '''
        helper.log.dbg('Processing donations feed...')
        for entry in feed.entries:
            item = {}
            item['link'] = entry.link
            item['date'] = helper.date.fmtdatetime.parse(entry.updated)
            item['text'] = helper.stringfmt.fmt_urls(entry.summary)
            item['title'] = entry.title
            self.data['donations'].append(item)

    def process_summary(self, feed):
        '''
        Reads summary feed and fills some useful information into data.
        '''
        helper.log.dbg('Processing summary feed...')
        data = {}
        links = {}
        trackers = []
        for entry in feed.entries:
            if entry.title[:22] == 'Developers on project:':
                m = SUMMARY_DEVS.match(entry.title)
                data['developers'] = m.group(1)
                links['developers'] = entry.link
            elif entry.title[:19] == 'Activity percentile':
                m = SUMMARY_ACTIVITY.match(entry.title)
                data['activity'] = m.group(1)
                links['activity'] = entry.link
            elif entry.title[:19] == 'Downloadable files:':
                m = SUMMARY_DOWNLOADS.match(entry.title)
                data['downloads'] = m.group(1)
                links['downloads'] = entry.link
            elif entry.title[:13] == 'Mailing lists':
                m = SUMMARY_LISTS.match(entry.title)
                data['mailinglists'] = m.group(1)
                links['mailinglists'] = entry.link
            elif entry.title[:17] == 'Discussion forums':
                m = SUMMARY_FORUMS.match(entry.title)
                data['forums'] = m.group(1)
                data['forumposts'] = m.group(2)
                links['forums'] = entry.link
            elif entry.title[:8] == 'Tracker:':
                m = SUMMARY_TRACKER.match(entry.title)
                trackers.append({
                    'name': m.group(1),
                    'open': m.group(2),
                    'total': m.group(3),
                    'description': entry.summary[21:],
                    'link': entry.link,
                })
        self.data['info'] = data
        self.data['links'] = links
        trackers.sort(key = lambda x: x['name'])
        self.data['trackers'] = trackers

    def get_menu(self, active):
        '''
        Returns list of menu entries with marked active one.
        '''
        menu = []
        for item in data.menu.MENU:
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
        helper.log.dbg('  %s' % filename)
        template = self.cssloader.load(filename)
        out = open(os.path.join(OUTPUT, 'css', filename), 'w')
        out.write(template.generate(**self.data).render())
        out.close()

    def render_static(self, templatename, outfile, extradata = {}):
        '''
        Renders "static" file from template.
        '''
        helper.log.dbg('  %s' % outfile)
        template = self.staticloader.load(templatename)
        out = open(os.path.join(OUTPUT, outfile), 'w')
        extradata.update(self.data)
        out.write(template.generate(**extradata).render())
        out.close()

    def render_js(self, filename):
        '''
        Renders JavaScript file from template. Some defined files are not processed
        through template engine as they were taken from other projects.
        '''
        helper.log.dbg('  %s' % filename)
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
        helper.log.dbg('  %s' % page)
        template = self.loader.load('%s.tpl' % page)
        menu = self.get_menu(page)
        out = open(os.path.join(OUTPUT, self.get_outname(page)), 'w')
        out.write(template.generate(menu = menu, **self.data).render(self.get_renderer(page)))
        out.close()

    def render_security(self, issue):
        '''
        Renders security issue.
        '''
        helper.log.dbg('  %s' % issue)
        template = self.loader.load('security/%s' % issue)
        menu = self.get_menu('security/')
        out = open(os.path.join(OUTPUT, 'security', self.get_outname(issue)), 'w')
        out.write(template.generate(menu = menu, issue = issue, **self.data).render('xhtml'))
        out.close()


    def list_security_issues(self):
        '''
        Fills in issues and topissues with security issues information.
        '''
        issues = glob.glob('templates/security/PMASA-*')
        issues.sort(key = lambda x: int(x[24:29]) * 100 - int(x[30:]))
        for issue in issues:
            data = XML(open(issue, 'r').read())
            name = os.path.basename(issue)
            self.data['issues'].append({
                'name' : name,
                'link': '%ssecurity/%s' % (BASE_URL, self.get_outname(name)),
                'fulllink': '%s%ssecurity/%s' % (SERVER, BASE_URL, self.get_outname(name)),
                'summary': str(data.select('def[@function="announcement_summary"]/text()')),
                'date': helper.date.fmtdate.parse(str(data.select('def[@function="announcement_date"]/text()'))),
                'cves': str(data.select('def[@function="announcement_cve"]/text()')).split(' '),
                'versions': str(data.select('def[@function="announcement_affected"]/text()')),
            })
        self.data['topissues'] = self.data['issues'][:TOP_ISSUES]

    def prepare_output(self):
        '''
        Copies static content to output and creates required directories.
        '''
        helper.log.dbg('Copying static content to output...')
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
        imgdst = os.path.join(OUTPUT, 'images')
        os.makedirs(imgdst)
        copytree(IMAGES, imgdst)
        copytree(STATIC, OUTPUT)
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
        elif page[:15] == '/documentation/':
            priority = '0.7'
            changefreq = 'weekly'
        elif page[:20] == '/pma_localized_docs/':
            priority = '0.6'
            changefreq = 'monthly'
        elif page in ['index', 'news']:
            priority = '1.0'
            changefreq = 'daily'
        elif page in ['improve', 'team', 'docs']:
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
            'lastmod' : helper.date.fmtdate.utcnow(),
            'changefreq' : changefreq,
            'priority' : priority,
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
            dir = root[len(TEMPLATES):].strip('/')
            if len(dir) > 0:
                dir += '/'
            for file in files:
                name, ext = os.path.splitext(file)
                if ext != '.tpl' and name[:6] != 'PMASA-':
                    continue
                if name[0] in ['_', '.']:
                    continue
                if file in ['index.xml.tpl', 'sitemap.xml.tpl', '404.tpl']:
                    continue
                helper.log.dbg('- %s' % file)
                xmldata = XML(open(os.path.join(root, file), 'r').read())
                title = str(xmldata.select('def[@function="page_title"]/text()'))
                title = title.strip()
                if len(title) == 0:
                    title = str(xmldata.select('def[@function="announcement_id"]/text()'))
                    title = title.strip()
                if len(title) == 0:
                    title = 'Index'
                link = dir + self.get_outname(name)
                sitemap = {
                        'link': link,
                        'loc': '%s%s%s' % (SERVER, BASE_URL, link),
                        'title': title
                        }
                if name[:6] != 'PMASA-':
                    self.data['sitemap'].append(sitemap)
                sitemap.update(self.get_sitemap_data(dir + name))
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
        list = self.git.langtree.keys()
        list.sort()
        for name in list:
            if name[-3:] != '.po':
                continue
            lang = name[:-3]
            longlang = data.langnames.MAP[lang]
            po = polib.pofile('cache/git___phpmyadmin.git.sourceforge.net_gitroot_phpmyadmin_phpmyadmin/po/%s' % name)
            helper.log.dbg(' - %s [%s]' % (lang, longlang))
            gitlog = self.git.repo.log(path = 'po/%s' % name)
            langs = '%s|%s' % (lang, longlang)
            regexp = re.compile(LANG_REGEXP % (langs, langs), re.IGNORECASE)
            found = None
            for x in gitlog:
                if regexp.findall(x.message) != []:
                    found = x
                    break

            percent = po.percent_translated()
            translated = len(po.translated_entries())
            if percent < 50:
                css = ' b50'
            elif percent < 80:
                css = ' b80'
            else:
                css =''
            try:
                dt = datetime.datetime(*found.committed_date[:6])
            except (TypeError, AttributeError):
                dt = ''
            self.data['translations'].append({
                'name': longlang,
                'short': lang,
                'translated': translated,
                'percent': '%0.1f' % percent,
                'updated': dt,
                'css': css,
            })

    def fetch_data(self):
        '''
        Fetches data from remote or local sources and prepares template data.
        '''
        self.get_snapshots_info()

        xml_files = self.xmls.load('files', PROJECT_FILES_RSS)

        self.process_releases(xml_files)
        self.process_themes(xml_files)

        rss_news = self.feeds.load('news', PROJECT_NEWS_RSS)
        self.process_news(rss_news)

        self.tweet()

        rss_planet = self.feeds.load('planet', PLANET_RSS)
        self.process_planet(rss_planet)

        rss_cz = self.feeds.load('cz', RSS_CZ)
        self.process_feed('news_cz', rss_cz)

        rss_ru = self.feeds.load('ru', RSS_RU)
        self.process_feed('news_ru', rss_ru)

        rss_summary = self.feeds.load('summary', PROJECT_SUMMARY_RSS)
        self.process_summary(rss_summary)

        rss_donations = self.feeds.load('donations', DONATIONS_RSS)
        self.process_donations(rss_donations)

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
        templates.extend([os.path.join('security', os.path.basename(x)) for x in glob.glob('templates/security/*.tpl')])
        for template in templates:
            name = os.path.splitext(template)[0]
            if os.path.basename(name)[0] == '_':
                continue
            self.render(name)

        helper.log.dbg('Rendering security issues pages:')
        for issue in self.data['issues']:
            self.render_security(issue['name'])

        helper.log.dbg('Generating CSS:')
        for css in [os.path.basename(x) for x in glob.glob('css/*.css')]:
            self.render_css(css)

        helper.log.dbg('Generating JavaScript:')
        for js in [os.path.basename(x) for x in glob.glob('js/*.js')]:
            self.render_js(js)

        helper.log.dbg('Generating static pages:')
        self.render_static('_version.php', 'version.php')
        self.render_static('_version.txt', 'version.txt')
        self.render_static('_security.php', 'security.php')
        self.render_static('_robots.txt', 'robots.txt')
        for redir in data.redirects.REDIRECTS:
            self.render_static('_redirect.tpl',
                '%s.php' % redir,
                {'location': self.get_outname(data.redirects.REDIRECTS[redir])})


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
    parser.add_option('-v', '--verbose',
                    action='store_true',
                    dest='verbose',
                    help='Output verbose information.')
    parser.add_option('-q', '--quiet',
                    action='store_false',
                    dest='verbose',
                    help='Only show errors and warnings.')
    parser.add_option('-C', '--clean',
                    action='store_true',
                    dest='clean',
                    help='Clean output directory (default).')
    parser.add_option('-N', '--no-clean',
                    action='store_false',
                    dest='clean',
                    help='Do  not clean output directory.')
    parser.add_option('-V', '--verbose-cache',
                    action='store_true',
                    dest='verbose_cache',
                    help='Output verbose caching information.')
    parser.add_option('-Q', '--quiet-cache',
                    action='store_false',
                    dest='verbose_cache',
                    help='No information from caching in output.')
    parser.add_option('-s', '--server',
                    action='store', type='string',
                    dest='server',
                    help='Name of server where data will be published, eg.: %s.' % SERVER)
    parser.add_option('-b', '--base-url',
                    action='store', type='string',
                    dest='base_url',
                    help='Base URL of document, eg.: %s.' % BASE_URL)
    parser.add_option('-e', '--extension',
                    action='store', type='string',
                    dest='extension',
                    help='Extension of generated files, default is %s.' % EXTENSION)
    parser.add_option('-l', '--log',
                    action='store', type='string',
                    dest='log',
                    help='Log filename, default is none.')
    parser.add_option('-p', '--identica-password',
                    action='store', type='string',
                    dest='identica_password',
                    help='Pasword to identi.ca, default is not to post there.')
    parser.add_option('-u', '--identica-user',
                    action='store', type='string',
                    dest='identica_user',
                    help='Username to identi.ca, defaull is %s.' % IDENTICA_USER)

    parser.set_defaults(
        verbose = helper.log.VERBOSE,
        verbose_cache = helper.log.DBG_CACHE,
        server = SERVER,
        base_url = BASE_URL,
        clean = CLEAN_OUTPUT,
        log = None,
        extension = EXTENSION,
        identica_user = IDENTICA_USER,
        identica_password = IDENTICA_PASSWORD
        )

    (options, args) = parser.parse_args()

    helper.log.VERBOSE = options.verbose
    helper.log.DBG_CACHE = options.verbose_cache
    SERVER = options.server
    BASE_URL = options.base_url
    EXTENSION = options.extension
    CLEAN_OUTPUT = options.clean
    IDENTICA_USER = options.identica_user
    IDENTICA_PASSWORD = options.identica_password
    if options.log is not None:
        helper.log.LOG = open(options.log, 'w')

    gen = SFGenerator()
    gen.main()
