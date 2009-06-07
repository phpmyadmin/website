# -*- coding: UTF-8 -*-
#
# phpMyAdmin web site generator
#  - caching module
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

import cPickle
import feedparser
import os
import time
import pysvn
import glob
import traceback
import urllib

import helper.log
import helper.date

# How long is cache valid (in seconds)
CACHE_TIME = 60 * 60
# How long is svn cache valid (in seconds)
SVN_CACHE_TIME = 60 * 60 * 24

class NoCache(Exception):
    pass

class Cache(object):
    '''
    Generic caching class.
    '''
    def __init__(self, timeout = CACHE_TIME):
        self._timeout = timeout

    def get_name(self, name, fnmask = '%s.dump'):
        '''
        Returns cache filename for given name.
        '''
        name = name.replace(':', '_').replace('/', '_').strip('_')
        return os.path.join('.', 'cache', fnmask % name)

    def check_timeout(self, filename):
        '''
        Checks whether filename is valid cache (not timeouted).
        '''
        try:
            mtime = os.path.getmtime(filename)
        except OSError:
            mtime = 0
        if mtime + self._timeout > time.time():
            return True
        return False

    def dbg(self, message):
        '''
        Logs messages if debugging is enabled.
        '''
        helper.log.dbg(message, 'cache')

    def warn(self, message):
        '''
        Shows a warning.
        '''
        helper.log.warn(message)

    def get(self, name):
        '''
        Loads cache if it is available and valid, raises exception otherwise.
        '''
        filename = self.get_name(name)
        if self.check_timeout(filename):
            self.dbg('Using cache for %s!' % name)
            try:
                return cPickle.load(open(filename, 'r'))
            except TypeError:
                # Cache can not be unpickled
                self.warn('Deleting cache for %s!' % name)
                os.unlink(filename)
                raise NoCache()
        raise NoCache()

    def force_get(self, name):
        '''
        Tries to load cache without any checks.
        '''
        filename = self.get_name(name)
        try:
            return cPickle.load(open(filename, 'r'))
        except IOError:
            raise NoCache()

    def set(self, name, data):
        '''
        Saves cache.
        '''
        filename = self.get_name(name)
        cPickle.dump(data, open(filename, 'w'))

class URLCache(Cache):
    '''
    URL caching class.
    '''
    def __init__(self, timeout = CACHE_TIME):
        super(URLCache, self).__init__(timeout)

    def load(self, url):
        self.dbg('Downloading %s...' % url)
        cache = 'url-%s' % url
        try:
            result = self.get(cache)
        except NoCache:
            result = urllib.urlopen(url).read()
            self.set(cache, result)
        return result

class FeedCache(URLCache):
    '''
    Feed caching class.
    '''
    def __init__(self, timeout = CACHE_TIME):
        super(FeedCache, self).__init__(timeout)

    def load(self, name, url):
        self.dbg('Downloading and parsing %s feed...' % name)
        self.dbg('URL: %s' % url)
        cache = 'feed-%s' % name
        try:
            result = self.get(cache)
        except NoCache:
            data = super(FeedCache, self).load(url)
            result = feedparser.parse(data.strip())
            if result.bozo == 1:
                self.warn('Feed %s is invalid: %s' % (url, str(result.bozo_exception)))
                try:
                    result = self.force_get(cache)
                    self.dbg('Using old cached version for %s' % cache)
                except:
                    raise result.bozo_exception
            else:
                self.set(cache, result)
        return result

class SimpleSVNCache(Cache):
    def __init__(self, url, timeout = SVN_CACHE_TIME):
        super(SimpleSVNCache, self).__init__(timeout)
        self._svn = pysvn.Client()
        self._url = url

    def cat(self, name):
        '''
        Performs cached svn cat, returns string with file content.
        '''
        fullname = '%s/%s' % (self._url, name)
        cachename = 'svn-log-%s' % fullname

        try:
            data = self.get(cachename)
            return data
        except NoCache:
            data = self._svn.cat(fullname)
            self.set(cachename, data)
            return data

    def log(self, name):
        '''
        Performs cached svn log, returs list of revisions as dict with
        message, date, author and revision fields.

        1. If cache is up to date, use cache.
        2. If cache exists, use it as base, request only remaining logs.
        3. Request missing logs.
        4. Save log to cache and return it.
        '''
        fullname = '%s/%s' % (self._url, name)
        cachename = 'svn-log-%s' % fullname

        try:
            list = self.get(cachename)
            return list
        except NoCache:
            pass

        try:
            list = self.force_get(cachename)
            base = list[0]['revision']
        except NoCache:
            list = []
            base = 0

        try:
            base_rev = pysvn.Revision(pysvn.opt_revision_kind.number, base)
            self.dbg('svn log -r %d %s' % (base, fullname))
            svnlog = self._svn.log(fullname, revision_end = base_rev)
            newlog = [{
                'message': x['message'],
                'revision': x['revision'].number,
                'date': helper.date.fmtdate.fromtimestamp(x['date']),
                'author': x['author'],
                } for x in svnlog]
            list.extend(newlog)
            list.sort(key = lambda x: x['revision'], reverse = True)
            self.set(cachename, list)
        except pysvn.ClientError:
            traceback.print_exc()
        return list

class SVNCache(SimpleSVNCache):
    def __init__(self, url, timeout = SVN_CACHE_TIME):
        super(SVNCache, self).__init__(timeout)
        self._svn = pysvn.Client()
        self._url = url
        self._updated = False
        self._wc = self.get_name('svn-%s' % self._url, '%s')

    def ls(self):
        '''
        Performs cached svn ls, returs list of URLs.
        '''
        self.update_wc()
        files = glob.glob(os.path.join(self._wc, '*'))
        files.sort()
        return [os.path.basename(x) for x in files]

    def cat(self, name):
        '''
        Performs cached svn cat, returns string with file content.
        '''
        self.update_wc()
        return open(os.path.join(self._wc, name), 'r').read()

    def update_wc(self):
        '''
        Updates working copy of repository.
        '''
        if self._updated:
            return
        if not os.path.exists(self._wc):
            self.dbg('svn co %s' % self._url)
            self._svn.checkout(self._url, self._wc)
            self._updated = True
        elif not self.check_timeout(self._wc):
            try:
                self.dbg('svn up %s' % self._url)
                self._svn.update(self._wc)
            except pysvn.ClientError:
                traceback.print_exc()
            self._updated = True
