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
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect
from security.models import PMASA


def redirect_security(request):
    """Redirect for old security page"""
    if 'issue' in request.GET:
        try:
            prefix, year, sequence = request.GET['issue'].split('-')
        except ValueError:
            return redirect('security')
        if prefix != 'PMASA':
            return redirect('security')

        try:
            return redirect(
                PMASA.objects.get(year=year, sequence=sequence)
            )
        except (PMASA.DoesNotExist, ValueError):
            return redirect('security')
    else:
        return redirect('security')


class PMASABaseView(DetailView):
    model = PMASA

    def get_context_data(self, **kwargs):
        context = super(PMASABaseView, self).get_context_data(**kwargs)
        context['page_title'] = 'Security - {0}'.format(self.object)
        context['page_rss'] = reverse('feed-security')
        context['page_rss_title'] = 'phpMyAdmin security announcements'
        context['pmasa_year'] = self.object.year
        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        queryset = queryset.filter(
            year=self.kwargs['year'],
            sequence=self.kwargs['sequence'],
        )

        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No PMASA found matching the query")


class PMASADraftView(PMASABaseView):
    def get_object(self, queryset=None):
        result = super(PMASADraftView, self).get_object(queryset)

        if not result.draft:
            raise Http404("No PMASA found matching the query")

        return result


class PMASAView(PMASABaseView):
    def get_object(self, queryset=None):
        result = super(PMASAView, self).get_object(queryset)

        if result.draft:
            raise Http404("No PMASA found matching the query")

        return result
