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

from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markupfield.fields import MarkupField
from pmaweb.cdn import purge_cdn


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        db_index=True, unique_for_date='date', max_length=100
    )
    date = models.DateTimeField(db_index=True, default=timezone.now)
    body = MarkupField(default_markup_type='markdown')
    author = models.ForeignKey(User, editable=False)

    class Meta(object):
        ordering = ['-date']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return (
            'news-item',
            (),
            {
                'day': self.date.day,
                'month': self.date.month,
                'year': self.date.year,
                'slug': self.slug,
            }
        )


class Planet(models.Model):
    """Cache for planet phpMyAdmin posts"""
    url = models.URLField(unique=True)
    title = models.CharField(max_length=150)
    date = models.DateTimeField(db_index=True, default=timezone.now)

    class Meta(object):
        ordering = ['-date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.url


@receiver(post_save, sender=Post)
def purge_post(sender, instance, **kwargs):
    num_pages = 1 + (Post.objects.count() / 10)
    pages = [
        reverse('home'),
        reverse('news'),
        reverse('feed-news'),
        instance.get_absolute_url(),
    ]
    pages.extend([
        reverse('news-page', kwargs={'page': x + 1})
        for x in range(num_pages)
    ])
    purge_cdn(*pages)


@receiver(post_save, sender=Planet)
def purge_planet(sender, instance, **kwargs):
    purge_cdn(reverse('home'))
