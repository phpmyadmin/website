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
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from markupfield.fields import MarkupField
import datetime
from pmaweb.cdn import purge_cdn

YEAR_TODAY = datetime.date.today().year
YEAR_CHOICES = [(i, i) for i in range(2003, YEAR_TODAY + 1)]


class PMASA(models.Model):
    year = models.IntegerField(
        choices=YEAR_CHOICES, default=YEAR_TODAY
    )
    sequence = models.IntegerField(
        help_text='Sequence number of PMASA in given year'
    )
    date = models.DateTimeField(db_index=True, default=timezone.now)
    updated = models.DateTimeField(
        null=True,
        blank=True,
        help_text='Set this in case of major update to the entry'
    )
    summary = models.CharField(max_length=200)
    description = MarkupField(default_markup_type='markdown')
    severity = models.TextField()
    mitigation = models.TextField(blank=True)
    affected = models.TextField()
    unaffected = models.TextField(blank=True)
    solution = models.TextField(
        max_length=200,
        default='Upgrade to phpMyAdmin ? or newer or apply patch listed below.'
    )
    references = models.TextField(
        help_text='Links to reporter etc.',
        blank=True,
    )
    cve = models.CharField(
        max_length=200,
        help_text='Space separated list of related CVE entries, enter CVE-2017- in case none is assigned yet'
    )
    cwe = models.CharField(
        max_length=200,
        default='661',
        help_text='Space separated list of CWE classifications'
    )
    commits = models.TextField(
        help_text=(
            'Space separated list of commits, commits for different branches '
            'should be placed on separate line prefixed with version prefix. '
            'For example: 3.5: 01d35b3558e47fba947719857bd71f6fd9e5dce8'
        )
    )
    draft = models.BooleanField(
        default=True,
        help_text='Draft entries are not shown in website listings'
    )

    class Meta(object):
        unique_together = ('year', 'sequence')
        ordering = ('-year', '-sequence')
        verbose_name = 'PMASA'
        verbose_name_plural = 'PMASAs'

    def __unicode__(self):
        return 'PMASA-{0}-{1}'.format(self.year, self.sequence)

    @models.permalink
    def get_absolute_url(self):
        if self.draft:
            page = 'security-issue-draft'
        else:
            page = 'security-issue'
        return (
            page,
            (),
            {'year': self.year, 'sequence': self.sequence}
        )

    def get_cves(self):
        for cve in self.cve.split():
            # Incomplete reference as CVE-2016-
            if cve[-1] == '-':
                yield '', 'Not yet assigned'
            else:
                yield 'https://cve.mitre.org/cgi-bin/cvename.cgi?name={0}'. format(cve), cve

    def get_cwes(self):
        return self.cwe.split()

    def get_commits(self):
        lines = self.commits.strip().split('\n')
        result = []
        for line in lines:
            if ':' in line:
                branch, line = line.split(':')
            else:
                branch = ''
            result.append({
                'branch': branch,
                'commits': line.strip().split(),
            })
        return result


@receiver(post_save, sender=PMASA)
def purge_pmasa(sender, instance, **kwargs):
    purge_cdn(
        reverse('security'),
        reverse('feed-security'),
        instance.get_absolute_url(),
    )
