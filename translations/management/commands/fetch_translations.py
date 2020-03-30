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
from translations.models import Translation
import json
from dateutil import parser
import urllib

URL = 'https://hosted.weblate.org/exports/stats/phpmyadmin/master/'


class Command(BaseCommand):
    help = 'Downloads translation stats'

    def handle(self, *args, **options):
        handle = urllib.urlopen(URL)
        data = handle.read()
        try:
            content = json.loads(data)
        except ValueError:
            print("There was a problem parsing the data from Hosted Weblate.")
            print("Check the status of the feed page: " + URL)
            import sys
            sys.exit(1)

        for item in content:
            updated = None
            if item['last_change']:
                updated = parser.parse(item['last_change'])
            params = {
                'name': item['name'],
                'translated': item['translated'],
                'percent': item['translated_percent'],
                'updated': updated,
            }
            translation, created = Translation.objects.get_or_create(
                url=item['url_translate'],
                defaults=params
            )
            if not created:
                modified = False
                for key in params:
                    if getattr(translation, key) != params[key]:
                        setattr(translation, key, params[key])
                        modified = True
                    if modified:
                        translation.save()
