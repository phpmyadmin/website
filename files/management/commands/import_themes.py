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

import os
import json
from zipfile import ZipFile

from django.core.management.base import BaseCommand
from django.conf import settings

from files.models import Theme
from files.utils import read_sum
from data.themes import THEMES


class Command(BaseCommand):
    help = 'Imports themes from filesystem'

    def process_theme(self, path, fullname):
        name, version, filename = fullname.split('/')
        namever = os.path.splitext(filename)[0]

        theme = Theme.objects.filter(
            filename=filename,
            name=name,
            version=version
        )
        if theme.exists():
            return

        zipfile = ZipFile(os.path.join(path, fullname), 'r')
        try:
            metadata = zipfile.open(os.path.join(name, 'theme.json'), 'r')
            data = json.load(metadata)
            data['support'] = ','.join(data['supports'])
            data['info' ] = data['description']
        except KeyError:
            self.stderr.write('Missing theme.json in {0}'.format(fullname))
            try:
                data = THEMES[namever]
            except KeyError:
                self.stderr.write('Unknown theme: {0}'.format(namever))
                self.stderr.write('Definition missing in website:data/themes.py')
                return

        complete_name = os.path.join(path, fullname)

        Theme.objects.get_or_create(
            filename=filename,
            name=name,
            version=version,
            defaults={
                'size': os.path.getsize(complete_name),
                'display_name': data['name'],
                'supported_versions': data['support'],
                'description': data['info'],
                'url': data['url'] if 'url' in data else '',
                'author': data['author'],
                'sha256': read_sum(
                    '{0}.sha256'.format(complete_name),
                    complete_name
                ),
                'sha1': read_sum(
                    '{0}.sha1'.format(complete_name),
                    complete_name
                ),
                'signed': os.path.exists('{0}.asc'.format(complete_name)),
            }
        )

    def handle(self, *args, **options):
        path = os.path.join(settings.FILES_PATH, 'themes')
        for root, dummy, files in os.walk(path):
            for filename in files:
                if filename.endswith(".zip"):
                    fullname = os.path.join(
                        root[len(path):].lstrip('/'), filename
                    )
                    self.process_theme(path, fullname)
