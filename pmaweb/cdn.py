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
"""CDN integration"""
from django.conf import settings
from urllib2 import urlopen
from urllib import urlencode
import json

URL = 'https://api.cdn77.com/v2.0/data/purge'
URL_ALL = 'https://api.cdn77.com/v2.0/data/purge-all'


def perform(url, data):
    """Perform CDN POST request"""
    handle = urlopen(url, urlencode(data))
    response = handle.read()
    decoded = json.loads(response)
    if decoded['status'] != 'ok':
        if 'errors' in decoded:
            raise Exception(decoded['errors'])
        raise Exception(decoded)
    return decoded


def purge_cdn(*pages):
    """Purges page on CDN"""
    if not settings.CDN_PASSWORD:
        return
    data = [
        ('login', settings.CDN_LOGIN),
        ('passwd', settings.CDN_PASSWORD),
        ('cdn_id', settings.CDN_ID),
    ]
    for page in pages:
        data.append(('url[]', page))
    return perform(URL, data)


def purge_files_cdn(*pages):
    """Purges page on CDN"""
    if not settings.CDN_PASSWORD:
        return
    data = [
        ('login', settings.CDN_LOGIN),
        ('passwd', settings.CDN_PASSWORD),
        ('cdn_id', settings.FILES_CDN_ID),
    ]
    for page in pages:
        data.append(('url[]', page))
    return perform(URL, data)


def purge_all_cdn():
    """Purges all pages on CDN"""
    if not settings.CDN_PASSWORD:
        return
    data = [
        ('login', settings.CDN_LOGIN),
        ('passwd', settings.CDN_PASSWORD),
        ('cdn_id', settings.CDN_ID),
    ]
    return perform(URL_ALL, data)
