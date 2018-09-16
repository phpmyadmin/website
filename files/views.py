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

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from files.models import Release, get_current_releases, Download
import json


class ReleaseList(ListView):
    model = Release

    def get_queryset(self):
        return Release.objects.filter(snapshot=False)

    def get_context_data(self, **kwargs):
        context = super(ReleaseList, self).get_context_data(**kwargs)
        context['page_title'] = 'Files'
        context['page_rss'] = reverse('feed-files')
        context['page_rss_title'] = 'phpMyAdmin releases'
        return context


class ReleaseDetail(DetailView):
    model = Release

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        queryset = queryset.filter(
            version=self.kwargs['version'],
        )

        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No release found matching the query")

    def get_context_data(self, **kwargs):
        context = super(ReleaseDetail, self).get_context_data(**kwargs)
        context['page_title'] = self.object.version
        context['page_rss'] = reverse('feed-files')
        context['page_rss_title'] = 'phpMyAdmin releases'
        return context


def version_json(request):
    latest = Release.objects.filter(stable=True)[0]
    response = {
        'version': latest.version,
        'date': latest.date.date().isoformat(),
        'releases': [],
    }
    for release in get_current_releases():
        response['releases'].append({
            'version': release.version,
            'date': release.date.date().isoformat(),
            'php_versions': release.get_php_versions(),
            'mysql_versions': release.get_mysql_versions(),
        })
    return HttpResponse(
        json.dumps(response, indent=4),
        content_type='application/json'
    )


def latest_download(request, flavor, extension, checksum=None):
    latest = Release.objects.filter(stable=True)[0]
    try:
        result = latest.download_set.get(
            filename__endswith='-{0}{1}'.format(flavor, extension)
        )
        if checksum == '.asc':
            return redirect(result.get_signed_url(), permanent=False)
        if checksum == '.sha256':
            return redirect(result.get_checksum_url(), permanent=False)
        return redirect(result, permanent=False)
    except Download.DoesNotExist:
        raise Http404("No release found matching the query")
