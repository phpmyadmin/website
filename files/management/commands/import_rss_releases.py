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

from django.core.management.base import BaseCommand
from xml.etree import ElementTree
import urllib
from dateutil import parser
from files.models import Release, Theme


URL = 'http://sourceforge.net/projects/phpmyadmin/rss?path=/&limit=10000'


class Command(BaseCommand):
    help = 'Imports themes metadata from sf.net'

    def process_item(self, item):
        filename = item.find('title').text
        if 'README.rst' in filename:
            return
        if filename.startswith('/phpMyAdmin/'):
            version = filename.split('/')[2]
            release = Release.objects.get(version=version)
        elif filename.startswith('/themes/'):
            theme = filename.split('/')[2]
            version = filename.split('/')[3]
            release = Theme.objects.get(name=theme, version=version)
        else:
            return

        datetext = item.find('pubDate').text
        # Fix timezone name
        if datetext.endswith(' UT'):
            datetext += 'C'
        date = parser.parse(datetext)
        if release.date != date:
            self.stdout.write(
                'Setting date of {0} from {1} to {2}'.format(
                    release, release.date, date
                )
            )
            release.date = date
            release.save()

    def handle(self, *args, **options):
        handle = urllib.urlopen(URL)
        data = handle.read()
        tree = ElementTree.fromstring(data)
        for item in tree.findall('channel/item'):
            self.process_item(item)
