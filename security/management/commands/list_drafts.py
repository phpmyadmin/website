# -*- coding: UTF-8 -*-
# vim: set expandtab sw=4 ts=4 sts=4:
#
# phpMyAdmin web site
#
# Copyright (C) 2008 - 2017 Michal Cihar <michal@cihar.com>
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
from django.utils.encoding import force_text

from security.models import PMASA


class Command(BaseCommand):
    help = 'Downloads demo server versions'

    def handle(self, *args, **options):
        for pmasa in PMASA.objects.filter(draft=True):
            name = force_text(pmasa)
            self.stdout.write(name)
            self.stdout.write('-' * len(name))
            self.stdout.write('')
            self.stdout.write('URL: https://www.phpmyadmin.net{0}'.format(pmasa.get_absolute_url()))
            self.stdout.write('Summary:\n{0}'.format(pmasa.summary))
            self.stdout.write('Affected:\n{0}'.format(pmasa.affected))
            self.stdout.write('Description:\n{0}'.format(pmasa.description))
            self.stdout.write('')
