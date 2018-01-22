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

from xml.etree import cElementTree as ElementTree
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.timezone import utc, make_aware
from urlparse import parse_qs
import httpretty
import datetime
from pmaweb.views import REDIRECT_MAP
from pmaweb.cdn import URL as CDN_URL, URL_ALL as CDN_URL_ALL
from files.models import Release, Download, Theme
from news.models import Post, Planet
from security.models import PMASA


class ViewTest(TestCase):
    fixtures = ['test_data.json']

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'phpMyAdmin')
        response = self.client.get('/')
        self.assertContains(response, 'phpMyAdmin')

    def test_pages(self):
        response = self.client.get(reverse('contractor'))
        self.assertContains(response, 'contract')

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
                'https://github.com/phpmyadmin/',
                msg_prefix='Invalid response for {0}'.format(url),
            )

    def test_sitemaps(self):
        # Get root sitemap
        response = self.client.get('/sitemap.xml')
        self.assertContains(response, '<sitemapindex')

        # Parse it
        tree = ElementTree.fromstring(response.content)
        sitemaps = tree.findall(
            '{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap'
        )
        for sitemap in sitemaps:
            location = sitemap.find(
                '{http://www.sitemaps.org/schemas/sitemap/0.9}loc'
            )
            response = self.client.get(location.text)
            self.assertContains(response, '<urlset')
            # Try if it's a valid XML
            ElementTree.fromstring(response.content)


class CDNTest(TestCase):
    trigger_urls = []

    def cdn_response(self, request, uri, headers):
        if uri == CDN_URL_ALL:
            self.trigger_urls.append('__ALL__')
        elif uri == CDN_URL:
            params = parse_qs(request.body.decode('utf-8'))
            self.trigger_urls.extend(params['url[]'])
        else:
            raise ValueError('Not supported URL: {0}'.format(uri))
        return (
            200, headers,
            '{"status":"ok"}',
        )

    @httpretty.activate
    def cdn_tester(self, model, urls, **kwargs):
        httpretty.register_uri(
            httpretty.POST,
            CDN_URL,
            body=self.cdn_response,
        )
        httpretty.register_uri(
            httpretty.POST,
            CDN_URL_ALL,
            body=self.cdn_response,
        )
        self.trigger_urls = []
        with self.settings(CDN_PASSWORD='x'):
            model.objects.create(**kwargs)
        for url in urls:
            self.assertIn(
                url,
                self.trigger_urls,
            )

    def test_pmasa(self):
        self.cdn_tester(
            PMASA,
            ['/security/', '/security/feed/', '/security/PMASA-2000-99/'],
            year=2000,
            sequence=99,
            draft=False,
        )

    def test_theme(self):
        self.cdn_tester(
            Theme,
            ['/themes/'],
            name='themeeee',
        )

    def test_release(self):
        self.cdn_tester(
            Release,
            [
                '/', '/news/', '/files/', '/files/feed/',
                '/downloads/', '/files/0.1/',
                '__ALL__',
            ],
            version='0.1',
        )

    def test_download(self):
        release = Release.objects.create(version='0.2')
        release.purged = False
        self.cdn_tester(
            Download,
            [
                '/', '/news/', '/files/', '/files/feed/',
                '/downloads/', '/files/0.2/',
                '__ALL__',
            ],
            release=release,
        )

    def test_news_post(self):
        self.cdn_tester(
            Post,
            ['/', '/news/', '/news/feed/', '/news/2000/1/1/slug/', '/news/1/'],
            title='title', slug='slug', author_id=0,
            date=make_aware(
                datetime.datetime(year=2000, month=1, day=1), utc
            ),
        )

    def test_news_planet(self):
        self.cdn_tester(
            Planet,
            ['/'],
            title='title', url='https://example.net/',
            date=make_aware(
                datetime.datetime(year=2000, month=1, day=1), utc
            ),
        )
