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
from django.db import models


class Translation(models.Model):
    url = models.URLField(unique=True)
    name = models.CharField(max_length=100)
    translated = models.IntegerField()
    percent = models.DecimalField(max_digits=4, decimal_places=1)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta(object):
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.url

    @property
    def css(self):
        if self.percent < 50:
            return 'progress-bar-danger'
        elif self.percent < 80:
            return 'progress-bar-warning'
        return 'progress-bar-success'
