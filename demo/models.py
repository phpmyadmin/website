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

from django.db import models
import re


QA_RE = re.compile(r'QA_([0-9]*)_([0-9]*)')
MAINT_RE = re.compile(r'MAINT_([0-9]*)_([0-9]*)_([0-9]*)')


class Demo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    master_version = models.CharField(max_length=100)

    def get_absolute_url(self):
        return u'https://demo.phpmyadmin.net/{0}/'.format(self.name)

    def get_login_url(self):
        if '-config' in self.name or '-http' in self.name:
            return None
        return u'{0}?pma_username=root'.format(self.get_absolute_url())

    def get_description(self):
        if self.name.startswith('master'):
            desc = []
            if '-config' in self.name:
                desc.append('Configured for config auth.')
            elif '-http' in self.name:
                desc.append('Configured for http auth.')
            else:
                desc.append('Configured for cookie auth.')
            if '-nopmadb' in self.name:
                desc.append(
                    'Without advanced features requiring extra database.'
                )
            return ' '.join(desc)
        if self.name == 'STABLE':
            return 'Latest phpMyAdmin stable release.'

        match = QA_RE.match(self.name)
        if match:
            return 'Maintenance branch for {0}.{1}.x releases.'.format(
                match.group(1),
                match.group(2),
            )

        match = MAINT_RE.match(self.name)
        if match:
            return 'Maintenance branch for {0}.{1}.{2} releases. This gets only urgent fixes.'.format(
                match.group(1),
                match.group(2),
                match.group(3),
            )

        return 'VERSION: {0}'.format(self.name)
