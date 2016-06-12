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

from django.contrib.syndication.views import Feed
from security.models import PMASA


class PMASAFeed(Feed):
    title = "phpMyAdmin security announcements"
    link = "/files/"
    description = "Security announcements from the phpMyAdmin project."
    description_template = 'security/rss.html'

    def items(self):
        return PMASA.objects.filter(draft=False)[:10]

    def item_title(self, item):
        return unicode(item)

    def item_pubdate(self, item):
        return item.date

    def item_author_name(self, item):
        return 'phpMyAdmin Security Team'
