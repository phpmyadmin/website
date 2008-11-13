# -*- coding: UTF-8 -*-
#
# phpMyAdmin web site generator
#  - date formatting and parsing
#
# Copyright (C) 2008 Michal Cihar <michal@cihar.com>
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

import datetime

class basedatetime(datetime.datetime):
    def w3cdtf(self):
        return self.strftime('%Y-%m-%dT%H:%M:%S+00:00')

class fmtdate(basedatetime):
    def __str__(self):
        return self.strftime('%Y-%m-%d')

    def parse(text):
        return fmtdate.strptime(text.strip(), '%Y-%m-%d')
    parse = staticmethod(parse)

class fmtdatetime(basedatetime):
    def __str__(self):
        return self.strftime('%a, %d %b %Y %H:%M:%S GMT')

    def parse(text):
        return fmtdatetime.strptime(text, '%a, %d %b %Y %H:%M:%S %Z')
    parse = staticmethod(parse)

