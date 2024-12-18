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

from collections import OrderedDict
from configparser import ConfigParser
import urllib.request, urllib.parse, urllib.error

from django.core.management.base import BaseCommand
from django.urls import reverse

from demo.models import Demo

from pmaweb.cdn import purge_cdn

URL = 'https://demo.phpmyadmin.net/versions.ini'


class MultiOrderedDict(OrderedDict):
    def __setitem__(self, key, value, dict_setitem=dict.__setitem__):
        if isinstance(value, list) and key in self:
            self[key].extend(value)
        else:
            # We intentionally skip parent class here
            dict_setitem(self, key, value)


class Command(BaseCommand):
    help = 'Downloads demo server versions'

    def handle(self, *args, **options):
        handle = urllib.request.urlopen(URL)
        config = ConfigParser(dict_type=MultiOrderedDict, strict=False, empty_lines_in_values=False, interpolation=None)
        try:
            config.read_string(handle.read().decode('utf-8'))
        except Exception as e:
            if hasattr(e, 'message'):
                print('Error:', e.message)
            else:
                print('Error:', e)
            print("Failed to read the version configuration file. ")
            print(("Check the status of " + URL))
            import sys
            sys.exit(1)

        master = config['demo']['master-release'][0]

        modified = False

        processed = set()

        for variant in config['demo']['variants[]']:
            demo, created = Demo.objects.get_or_create(
                name=variant.split(':')[0],
                defaults={'master_version': master}
            )
            modified |= created
            if not created and demo.master_version != master:
                demo.master_version = master
                demo.save()
                modified = True

            processed.add(demo.id)

        Demo.objects.exclude(id__in=processed).delete()

        if modified:
            purge_cdn(reverse('try'))
