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
from django.test import TestCase
from security.models import PMASA


class PMASATest(TestCase):
    def test_commits(self):
        self.assertEqual(
            PMASA(commits='1234\n3.3: 4312').get_commits(),
            [
                {'commits': ['1234'], 'branch': ''},
                {'commits': ['4312'], 'branch': '3.3'},
            ]
        )
        self.assertEqual(
            PMASA(commits='1234\n3.3: 4312\n4.4: 6667').get_commits(),
            [
                {'commits': ['1234'], 'branch': ''},
                {'commits': ['4312'], 'branch': '3.3'},
                {'commits': ['6667'], 'branch': '4.4'},
            ]
        )
