# -*- coding: UTF-8 -*-
#
# phpMyAdmin web site generator
#  - logging
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

import sys

# Enable verbose messages?
VERBOSE = True
# Debug cache
DBG_CACHE = True

def warn(text):
    '''
    Issues warning to stderr.
    '''
    sys.stderr.write('%s\n' % text)

def dbg(text, type = None):
    '''
    Prints debug information to stderr.
    '''
    if type is not None:
        if type == 'cache' and DBG_CACHE:
            sys.stderr.write('%s\n' % text)
    else:
        if VERBOSE:
            sys.stderr.write('%s\n' % text)

