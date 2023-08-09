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
#

from django.test import TestCase
from files.models import Release
from files.models import Download


class ReleaseTest(TestCase):
    def test_version(self):
        self.assertEqual(
            Release.parse_version('1.2.3.1'),
            102030199
        )
        self.assertEqual(
            Release.parse_version('1.2'),
            102000099
        )
        self.assertEqual(
            Release.parse_version('1.2.3'),
            102030099
        )
        self.assertEqual(
            Release.parse_version('1.2.3-rc1'),
            102030051
        )
        self.assertEqual(
            Release.parse_version('1.2.3-beta9'),
            102030019
        )
        self.assertEqual(
            Release.parse_version('1.2.3-alpha2'),
            102030002
        )

    def test_urls(self):
        r = Release()
        r.version = "1.2.3"
        d = Download()
        d.release = r
        d.filename = "english.zip"
        self.assertEqual(
            d.get_checksum_url(),
            'https://files.phpmyadmin.net/phpMyAdmin/1.2.3/english.zip.sha256'
        )
        self.assertEqual(
            d.get_signed_url(),
            ''
        )
        d.signed = True
        self.assertEqual(
            d.get_signed_url(),
            'https://files.phpmyadmin.net/phpMyAdmin/1.2.3/english.zip.asc'
        )
        self.assertEqual(
            d.get_absolute_url(),
            'https://files.phpmyadmin.net/phpMyAdmin/1.2.3/english.zip'
        )
        self.assertEqual(
            d.archive,
            'zip'
        )
        self.assertEqual(
            d.composer_type,
            'zip'
        )
        d.filename = 'english.xz'
        self.assertEqual(
            d.composer_type,
            'tar'
        )
        d.filename = 'english.zip'
        self.assertEqual(
            d.composer_type,
            'zip'
        )
        self.assertEqual(
            d.is_featured,
            False
        )
        d.filename = 'all-languages.zip'
        self.assertEqual(
            d.is_featured,
            True
        )
        d.filename = 'english.zip'
        self.assertEqual(
            d.is_featured,
            False
        )
        d.filename = 'phpMyAdmin-latest-all-languages.zip'
        self.assertEqual(
            d.get_stable_url,
            '/downloads/phpMyAdmin-latest-all-languages.zip'
        )
        self.assertEqual(
            d.get_stable_filename,
            'phpMyAdmin-latest-all-languages.zip'
        )
        d.filename = 'phpMyAdmin-latest-all-languages.tar.xz'
        self.assertEqual(
            d.get_stable_filename,
            'phpMyAdmin-latest-all-languages.tar.xz'
        )

