# -*- coding: UTF-8 -*-
# vim: set expandtab sw=4 ts=4 sts=4:
#
# phpMyAdmin web site
#
# Copyright (C) 2008 - 2016 Michal Cihar <michal@cihar.com>
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
#
from django.core.management.base import BaseCommand, CommandError
import feedparser
import urllib.request

def fetch_url(url: str) -> feedparser.FeedParserDict:
    """Helper for fetch blog posts"""
    try:
        request = urllib.request.Request(url)
        request.add_header('User-Agent', 'phpMyAdmin/website blog post fetcher')
        handle = urllib.request.urlopen(request)
        content = handle.read()
    except IOError as err:
        content = str(err)
        if hasattr(err, 'fp'):
            content = err.fp.read()
        raise CommandError(f'[{url}] {err.code}: {content}')
    return feedparser.parse(content)

class FeedCommand(BaseCommand):
    url: str = ''

    def process_feed(self, feed):
        raise NotImplementedError()

    def handle(self, *args, **options):
        parsed = fetch_url(self.url)
        self.process_feed(parsed)
