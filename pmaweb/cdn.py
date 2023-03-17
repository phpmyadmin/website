# -*- coding: UTF-8 -*-
# vim: set expandtab sw=4 ts=4 sts=4:
#
# phpMyAdmin web site
#
# Copyright (C) 2008 - 2016 Michal Cihar <michal@cihar.com>
# Copyright (C) 2022 William Desportes <williamdes@wdes.fr>
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

import urllib2
import json

URL = 'https://api.cdn77.com/v3/cdn/{id}/job/purge'
URL_ALL = 'https://api.cdn77.com/v3/cdn/{id}/job/purge-all'


def perform(url, paths):
    """Perform CDN POST request"""

    data = json.dumps({'paths': paths}).encode('utf-8')
    req = urllib2.Request(url, data, {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer {token}'.replace('{token}', settings.CDN_API_TOKEN),
            'User-Agent': 'phpMyAdmin/website script',
        })

    handle = urllib2.urlopen(req)
    response = handle.read()
    decoded = json.loads(response)
    handle.close()

    if decoded['state'] != 'done' and decoded['state'] != 'queued':
        if 'errors' in decoded:
            raise Exception(decoded['errors'])
        raise Exception(decoded)
    return decoded


def purge_cdn(*pages):
    """Purges page on CDN"""
    if not settings.CDN_API_TOKEN:
        return

    return perform(URL.replace('{id}', settings.CDN_ID), pages)


def purge_files_cdn(*pages):
    """Purges page on CDN"""
    if not settings.CDN_API_TOKEN:
        return

    return perform(URL.replace('{id}', settings.FILES_CDN_ID), pages)


def purge_all_cdn():
    """Purges all pages on CDN"""
    if not settings.CDN_API_TOKEN:
        return

    return perform(URL_ALL.replace('{id}', settings.CDN_ID), [])

