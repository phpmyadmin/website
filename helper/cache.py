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
import glob
import traceback
import urllib
import git

from xml.dom import minidom

import helper.log
import helper.date

# How long is cache valid (in seconds)
CACHE_TIME = 60 * 60

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
            except (TypeError, EOFError):
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
            try:
                result = urllib.urlopen(url).read()
                if result == '':
                    result = self.force_get(cache)
                else:
                    self.set(cache, result)
            except IOError:
                result = self.force_get(cache)
        return result

class XMLCache(URLCache):
    '''
    XML caching class.
    '''
    def __init__(self, timeout = CACHE_TIME):
        super(XMLCache, self).__init__(timeout)

    def load(self, name, url):
        self.dbg('Downloading and parsing %s feed...' % name)
        self.dbg('URL: %s' % url)
        data = super(XMLCache, self).load(url)
        return minidom.parseString(data.strip())

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

class GitCache(Cache):
    def __init__(self, url):
        self.dirname = self.get_name(url, '%s')
        if not os.path.exists(self.dirname):
            os.system('git clone %s %s' % (url, self.dirname))
        else:
            os.system('cd %s ; git pull -q' % self.dirname)
        self.repo = git.Repo(self.dirname)
        self.tree = self.repo.tree()
        self.langtree = self.tree['po']
