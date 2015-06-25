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
"""Compatibility redirect handlers"""

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import render


REDIRECT_MAP = {
    # Historical pages
    'books': 'docs',
    'demos': 'try',
    'feedback': 'support',
    'relnotes': 'news',
    'stats': 'team',

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
    'search': 'search',
    'sitemap': 'sitemap',
    'sponsors': 'sponsors',
    'support': 'support',
    'team': 'team',
    'themes': 'themes',
    'translate': 'translate',
    'translations': 'translations',
    'try': 'try',
}


def redirect_home_page(request, page):
    """Redirect handled for old website links"""
    try:
        return redirect(REDIRECT_MAP[page], permanent=True)
    except KeyError:
        raise Http404('Not existing page: {0}'.format(page))


def redirect_security(request):
    """Redirect for old security page"""
    if 'issue' in request.GET:
        prefix, year, sequence = request.GET['issue'].split('-')
        return redirect('security-issue', year=year, sequence=sequence)
    else:
        return redirect('security')


def notfound(request):
    return render(
        request,
        '404.html',
        {'title': 'Page Not Found'},
        status=404
    )


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
