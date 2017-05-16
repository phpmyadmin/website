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

from django.contrib import admin
from files.models import Release, Download, Theme


class ReleaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('version', 'stable', 'date')
    search_fields = ('version',)


class DownloadAdmin(admin.ModelAdmin):
    list_display = ('filename', 'release', 'size', 'signed')
    search_fields = ('filename',)


class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'display_name', 'version', 'filename', 'supported_versions', 'size',
        'show',
    )
    list_filter = ('supported_versions', 'show')
    actions = ('do_show', 'do_hide')

    def do_show(self, request, queryset):
        queryset.update(show=True)
    do_show.short_description = "Mark selected themes as shown"

    def do_hide(self, request, queryset):
        queryset.update(show=False)
    do_hide.short_description = "Mark selected themes as hidden"


admin.site.register(Release, ReleaseAdmin)
admin.site.register(Download, DownloadAdmin)
admin.site.register(Theme, ThemeAdmin)
