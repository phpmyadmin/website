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
from django.core.urlresolvers import reverse
from demo.models import Demo
from ConfigParser import RawConfigParser
from pmaweb.cdn import purge_cdn
import urllib
from collections import OrderedDict

URL = 'http://demo.phpmyadmin.net/versions.ini'


class MultiOrderedDict(OrderedDict):
    def __setitem__(self, key, value):
        if isinstance(value, list) and key in self:
            self[key].extend(value)
        else:
            super(OrderedDict, self).__setitem__(key, value)


class Command(BaseCommand):
    help = 'Downloads demo server versions'

    def handle(self, *args, **options):
        handle = urllib.urlopen(URL)
        config = RawConfigParser(dict_type=MultiOrderedDict)
        config.readfp(handle)

        master = config.get('demo', 'master-release')[0]

        modified = False

        processed = set()

        for version in config.get('demo', 'branches[]'):
            demo, created = Demo.objects.get_or_create(
                name=version,
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
