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
phpMyAdmin web site generator - date formatting and parsing.
'''

import datetime
import dateutil.parser


class DateTime(datetime.datetime):
    def w3cdtf(self):
        return self.strftime('%Y-%m-%dT%H:%M:%S+00:00')

    def datestring(self):
        return self.strftime('%Y-%m-%d')

    @staticmethod
    def parse(text):
        default = DateTime.now().replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        return dateutil.parser.parse(text, default=default)

    def __str__(self):
        return self.datestring()
