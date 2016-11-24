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
from django.db.models import Q
from hashlib import sha256, sha1
from files.models import Download, Theme


class Command(BaseCommand):
    help = 'Calculates missing checksums for releases'

    def add_sums(self, item):
        with open(item.get_filesystem_path(), 'r') as handle:
            data = handle.read()

        if item.sha256 == '':
            item.sha256 = sha256(data).hexdigest()

        if item.sha1 == '':
            item.sha1 = sha1(data).hexdigest()

        item.save()

    def handle(self, *args, **options):
        query = Q(sha256='') | Q(sha1='')
        for item in Theme.objects.filter(query):
            self.add_sums(item)
        for item in Download.objects.filter(query):
            self.add_sums(item)
