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
from django.core.urlresolvers import reverse
from pmaweb.views import REDIRECT_MAP, redirect_home_page


class ViewTest(TestCase):
    fixtures = ['test_data.json']

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'phpMyAdmin')
        response = self.client.get('/')
        self.assertContains(response, 'phpMyAdmin')

    def test_themes(self):
        response = self.client.get(reverse('themes'))
        self.assertContains(response, 'Metro')

    def test_redirects(self):
        for url in REDIRECT_MAP:
            response = self.client.get(
                '/home_page/{0}.php'.format(url),
                follow=True
            )
            self.assertContains(
                response,
                'http://github.com/phpmyadmin/',
                msg_prefix='Invalid response for {0}'.format(url),
            )

    def test_security_redirect(self):
        # TODO: remove fetch_redirect_response once these pages are implemented
        response = self.client.get('/home_page/security.php')
        self.assertRedirects(response, '/security/', fetch_redirect_response=False)
        response = self.client.get('/home_page/security.php?issue=PMASA-2011-1')
        self.assertRedirects(response, '/security/PMASA-2011-1/', fetch_redirect_response=False)
