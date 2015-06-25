# -*- coding: UTF-8 -*-
# vim: set expandtab sw=4 ts=4 sts=4:
#
# phpMyAdmin web site
#
# Copyright (C) 2008 - 2015 Michal Cihar <michal@cihar.com>
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

from django.core.management.base import BaseCommand
import feedparser
from dateutil import parser
import urllib
from news.models import Planet

URL = 'http://planet.phpmyadmin.net/rss20.xml'


class Command(BaseCommand):
    help = 'Imports planet posts'

    def process_feed(self, feed):
        for entry in feed.entries:
            params = {
                'title': entry.title,
                'date': parser.parse(entry.published),
            }
            planet, created = Planet.objects.get_or_create(
                url=entry.link,
                defaults=params
            )
            if not created:
                continue

            modified = False
            for key in params:
                if getattr(planet, key) != params[key]:
                    setattr(planet, key, params[key])
                    modified = True
            if modified:
                planet.save()

    def handle(self, *args, **options):
        handle = urllib.urlopen(URL)
        data = handle.read()
        parsed = feedparser.parse(data)
        if parsed.bozo == 1:
            raise CommandError(parsed.bozo_exception)
        else:
            self.process_feed(parsed)
