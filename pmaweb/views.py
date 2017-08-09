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
"""Compatibility redirect handlers"""

import urllib2
import base64

from django.conf import settings
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseServerError
from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView
from django.shortcuts import render

# Aliases to redirect from old website URLs (/home_page/something.php)
# to new ones (/something/):

REDIRECT_MAP = {
    # Historical pages
    'books': 'docs',
    'demos': 'try',
    'feedback': 'support',
    'relnotes': 'news',
    'stats': 'team',
    'sitemap': 'home',
    'gophp5': 'home',
    'search': 'home',

    # Alive pages
    '15-years': '15-years',
    'about-website': 'about-website',
    'about': 'about',
    'awards': 'awards',
    'contest': 'contest',
    'devel': 'develop',
    'docs': 'docs',
    'donate': 'donate',
    'downloads': 'downloads',
    'improve': 'contribute',
    'index': 'home',
    'license': 'license',
    'news': 'news',
    'sponsors': 'sponsors',
    'support': 'support',
    'team': 'team',
    'themes': 'themes',
    'translate': 'translate',
    'translations': 'translations',
    'try': 'try',

    # Broken links
    'ownloads': 'downloads',
}

GITHUB_API = 'https://api.github.com/repos/phpmyadmin/phpmyadmin/git/'


def redirect_home_page(request, page):
    """Redirect handled for old website links"""
    try:
        return redirect(REDIRECT_MAP[page], permanent=True)
    except KeyError:
        raise Http404('Not existing page: {0}'.format(page))


def notfound(request):
    return render(
        request,
        '404.html',
        {'title': 'Page Not Found'},
        status=404
    )


def proxy_request(url):
    """Helper for proxying requests"""
    try:
        request = urllib2.Request(url)
        if settings.GITHUB_USER and settings.GITHUB_TOKEN:
            base64string = base64.b64encode('%s:%s' % (settings.GITHUB_USER, settings.GITHUB_TOKEN))
            request.add_header('Authorization', 'Basic %s' % base64string)
        handle = urllib2.urlopen(request)
        code = handle.getcode()
        content = handle.read()
    except IOError as err:
        content = str(err)
        if hasattr(err, 'fp'):
            content = err.fp.read()
        if hasattr(err, 'code') and err.code == 404:
            raise Http404(content)
        return HttpResponseServerError(content)
    return HttpResponse(
        content,
        content_type='application/json',
    )


@cache_control(max_age=600)
def github_tree(request, name):
    """Proxy for GitHub tree API"""
    return proxy_request('{0}trees/{1}'.format(GITHUB_API, name))


@cache_control(max_age=86400)
def github_commit(request, name):
    """Proxy for GitHub commit API"""
    return proxy_request('{0}commits/{1}'.format(GITHUB_API, name))


class PMAView(TemplateView):
    title = ''
    rss = ''
    rss_title = ''

    def __init__(self, *args, **kwargs):
        self.title = kwargs.pop('title', '')
        self.rss = kwargs.pop('rss', 'feed-news')
        if '/' not in self.rss:
            self.rss = reverse(self.rss)
        self.rss_title = kwargs.pop('rss_title', 'phpMyAdmin news')
        super(PMAView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PMAView, self).get_context_data(**kwargs)
        context['page_title'] = self.title
        context['page_rss'] = self.rss
        context['page_rss_title'] = self.rss_title
        return context
