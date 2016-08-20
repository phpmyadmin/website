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


import os

from django.template import Library
from django.utils.html import escape
from django.utils.safestring import mark_safe

from files.models import Release

register = Library()


@register.simple_tag
def releaselink(name):
    try:
        release = Release.objects.get(version=name)
        return mark_safe(
            '<a href="{0}">{1}</a>'.format(
                escape(release.get_absolute_url()),
                escape(release.version)
            )
        )
    except:
        return name
