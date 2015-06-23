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

from files.models import Release, Theme
from news.models import Post
from security.models import PMASA
from django.conf import settings
from django.core.urlresolvers import reverse
import datetime

from data.menu import MENU
from data.screenshots import SCREENSHOTS
from data.themes import CSSVERSIONS
from data.awards import AWARDS


def basic(request):
    return {
        'current_year': datetime.datetime.now().year,
        'short_news': Post.objects.all()[:5],
        'screenshots': SCREENSHOTS,
        'themes': Theme.objects.all(),
        'themecssversions': CSSVERSIONS,
        'awards': AWARDS,
        'pmasas': PMASA.objects.filter(draft=False),
    }


def menu(request):
    result = []

    for name, title in MENU:
        if name:
            urlname = name.rstrip('/')
        else:
            urlname = 'home'

        active = (
            request.resolver_match and
            urlname == request.resolver_match.url_name
        )

        result.append({
            'title': title,
            'url': reverse(urlname),
            'active': active,
        })

    return {
        'menu': result,
    }


def releases(request=None):

    latest = Release.objects.filter(stable=True)[0]
    beta = Release.objects.filter(stable=False)[0]
    if beta.version_num < latest.version_num:
        beta = None

    delta = 1000000
    releases = []

    for version in settings.LISTED_BRANCHES:
        min_vernum = Release.parse_version(version)
        max_vernum = min_vernum + delta
        releases.append(Release.objects.filter(
            version_num__gte=min_vernum,
            version_num__lt=max_vernum,
            stable=True,
        )[0])

    return {
        'latest': latest,
        'beta': beta,
        'releases': releases,
    }
