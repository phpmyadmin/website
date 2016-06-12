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
from django.views.generic.dates import ArchiveIndexView, DateDetailView
from news.models import Post


class PostArchive(ArchiveIndexView):
    model = Post
    date_field = 'date'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PostArchive, self).get_context_data(**kwargs)
        context['page_title'] = 'News'
        return context

    def paginate_queryset(self, queryset, page_size):
        # We don't want to page parameter from GET to be used
        if 'page' not in self.kwargs:
            self.kwargs['page'] = '1'
        return super(PostArchive, self).paginate_queryset(queryset, page_size)


class PostDetail(DateDetailView):
    model = Post
    date_field = 'date'
    month_format = '%m'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['page_title'] = self.object.title
        return context
