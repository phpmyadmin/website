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

from django.contrib.sitemaps import GenericSitemap, Sitemap
from django.core.urlresolvers import reverse
from django.utils import timezone
from news.models import Post
from security.models import PMASA
from files.models import Release


class PagesSitemap(Sitemap):
    changefreq = 'weekly'

    def items(self):
        return [
            ('support', 1),
            ('docs', 1),
            ('try', 1),
            ('contribute', 1),
            ('sponsors', 0.5),
            ('license', 0.2),
            ('team', 0.5),
            ('translations', 0.2),
            ('awards', 0.5),
            ('about', 0.2),
            ('15-years', 0.8),
            ('donate', 0.5),
            ('about-website', 0.2),
            ('translate', 1),
            ('develop', 1),
            ('contest', 0.1),
        ]

    def location(self, item):
        return reverse(item[0])

    def lastmod(self, item):
        return None

    def priority(self, item):
        return item[1]


class DailySitemap(PagesSitemap):
    changefreq = 'daily'

    def items(self):
        return [
            ('home', 1),
            ('news', 1),
            ('security', 1),
            ('downloads', 1),
            ('themes', 0.8),
            ('files', 0.5),
        ]


class NewsSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return Post.objects.filter(date__lt=timezone.now())

    def lastmod(self, item):
        return item.date


class SecuritySitemap(Sitemap):
    priority = 1
    changefreq = 'weekly'

    def items(self):
        return PMASA.objects.filter(draft=False)

    def lastmod(self, item):
        return item.date


class ReleasesSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return Release.objects.filter(snapshot=False)

    def lastmod(self, item):
        return item.date


SITEMAPS = {
    'news': NewsSitemap(),
    'security': SecuritySitemap(),
    'releases': ReleasesSitemap(),
    'pages': PagesSitemap(),
    'daily': DailySitemap(),
}
