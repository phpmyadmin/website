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
'''
phpMyAdmin web site generator - String formatting helper.
'''

import re


def fmt_urls(text):
    '''
    Formats urls in input as HTML hyperlinks.
    '''
    # Escape any HTML
    text = text.replace(
        '&', '&amp;'
    ).replace(
        '<', '&lt;'
    ).replace(
        '>', '&gt;'
    )
    # Guess something what looks like an URL
    text = re.sub(
        r'(([a-z0-9A-Z_-]+\.)+[a-z0-9A-Z_-]+(/[^ ]*[^,.-;: )>])?)',
        'http://\\1',
        text
    )
    # Fixup what we might make wrong in previous guess
    text = re.sub(
        '((ht|f)tps?://)http://',
        '\\1',
        text
    )
    # Hyperlinks to html
    text = re.sub(
        '(((ht|f)tps?)://[^ "]*[^,.-;: )>"])',
        '<a href="\\1" rel="nofollow">\\1</a>',
        text
    )
    return text
