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

import json
import urllib2
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils import timezone
import os.path
from data.themes import CSSMAP
from markupfield.fields import MarkupField
from pmaweb.cdn import purge_cdn, purge_all_cdn

# Naming of versions
VERSION_INFO = (
    ('alpha1', ' First alpha version.'),
    ('alpha2', ' Second alpha version.'),
    ('alpha3', ' Third alpha version.'),
    ('alpha4', ' Fourth alpha version.'),
    ('beta1', ' First beta version.'),
    ('beta2', ' Second beta version.'),
    ('beta3', ' Third beta version.'),
    ('beta4', ' Fourth beta version.'),
    ('beta', ' Beta version.'),
    ('rc1', ' First release candidate.'),
    ('rc2', ' Second release candidate.'),
    ('rc3', ' Third release candidate.'),
    ('rc4', ' Fourth release candidate.'),
    ('rc', ' Release candidate.'),
)

DOCKER_TRIGGER = \
    'https://registry.hub.docker.com/u/phpmyadmin/phpmyadmin/trigger/{0}/'


def get_current_releases():
    delta = 1000000
    result = []

    for version in settings.LISTED_BRANCHES:
        min_vernum = Release.parse_version(version)
        max_vernum = min_vernum + delta
        stable_releases = Release.objects.filter(
            version_num__gte=min_vernum,
            version_num__lt=max_vernum,
            stable=True,
        )
        if stable_releases.exists():
            result.append(stable_releases[0])

    return result


class Release(models.Model):
    version = models.CharField(max_length=50, unique=True)
    version_num = models.IntegerField(default=0, unique=True)
    release_notes = MarkupField(default_markup_type='markdown')
    stable = models.BooleanField(default=False, db_index=True)
    snapshot = models.BooleanField(default=False, db_index=True)
    date = models.DateTimeField(db_index=True, default=timezone.now)

    purged = False

    class Meta(object):
        ordering = ['-version_num']

    def __unicode__(self):
        return self.version

    def get_absolute_url(self):
        if self.snapshot:
            return reverse('downloads')
        return reverse('release', kwargs={'version': self.version})

    def simpledownload(self):
        try:
            return self.download_set.get(
                filename__endswith='-all-languages.zip'
            )
        except Download.DoesNotExist:
            try:
                return self.download_set.all()[0]
            except IndexError:
                return None

    @staticmethod
    def parse_version(version):
        if '+' in version:
            # Snapshots, eg. 4.7+snapshot
            parts = [int(x) for x in version.split('+')[0].split('.')]
            assert len(parts) == 2
            return (
                100000000 * parts[0] +
                1000000 * parts[1]
            )
        if '-' in version:
            version, suffix = version.split('-')
            if suffix.startswith('alpha'):
                suffix_num = int(suffix[5:])
            elif suffix.startswith('beta'):
                suffix_num = 10 + int(suffix[4:])
            elif suffix.startswith('rc'):
                suffix_num = 50 + int(suffix[2:])
            else:
                raise ValueError(version)
        else:
            suffix_num = 99
            version = version
        parts = [int(x) for x in version.split('.')]
        if len(parts) == 2:
            parts.append(0)
        if len(parts) == 3:
            parts.append(0)
        assert len(parts) == 4
        return (
            100000000 * parts[0] +
            1000000 * parts[1] +
            10000 * parts[2] +
            100 * parts[3] +
            suffix_num
        )

    def save(self, *args, **kwargs):
        self.version_num = self.parse_version(self.version)
        self.stable = self.version_num % 100 == 99
        super(Release, self).save(*args, **kwargs)

    def get_version_suffix(self):
        '''
        Returns suffix for a version.
        '''
        for match, result in VERSION_INFO:
            if self.version.find(match) != -1:
                return result
        return ''

    def get_php_versions(self):
        if self.version[:3] == '5.1':
            return '>=7.1,<8.0'
        elif self.version[:3] == '5.0':
            return '>=7.1,<8.0'
        elif self.version[:3] == '4.9':
            return '>=5.5,<8.0'
        elif self.version[:3] == '4.8':
            return '>=5.5,<7.3'
        elif self.version[:3] == '4.7':
            return '>=5.5,<7.3'
        elif self.version[:3] == '4.6':
            return '>=5.5,<7.2'
        elif self.version[:3] == '4.5':
            return '>=5.5,<7.1'
        elif self.version[:3] == '4.4':
            return '>=5.3,<7.1'
        elif self.version[:3] == '4.3':
            return '>=5.3,<7.0'
        elif self.version[:3] == '4.2':
            return '>=5.3,<7.0'
        elif self.version[:3] == '4.1':
            return '>=5.3,<7.0'
        elif self.version[:3] == '4.0':
            return '>=5.2,<5.3'

    def get_mysql_versions(self):
        if self.version[:3] == '5.1':
            return '>=5.5'
        elif self.version[:3] == '5.0':
            return '>=5.5'
        elif self.version[:3] == '4.9':
            return '>=5.5'
        elif self.version[:3] == '4.8':
            return '>=5.5'
        elif self.version[:3] == '4.7':
            return '>=5.5'
        elif self.version[:3] == '4.6':
            return '>=5.5'
        elif self.version[:3] == '4.5':
            return '>=5.5'
        elif self.version[:3] == '4.4':
            return '>=5.5'
        elif self.version[:3] == '4.3':
            return '>=5.5'
        elif self.version[:3] == '4.2':
            return '>=5.5'
        elif self.version[:3] == '4.1':
            return '>=5.5'
        elif self.version[:3] == '4.0':
            return '>=5.0'

    def get_version_info(self):
        '''
        Returns description to the phpMyAdmin version.
        '''
        text = ''
        if self.version[:2] == '0.':
            text = 'Historical release.'
        elif self.version[:2] == '1.':
            text = 'Historical release.'
        elif self.version[:2] == '2.':
            text = 'Version compatible with PHP 4+ and MySQL 3+.'
        elif self.version[:2] == '3.':
            text = (
                'Frames version not requiring Javascript. ' +
                'Requires PHP 5.2 and MySQL 5. ' +
                'Supported for security fixes only, until Jan 1, 2014.'
            )
        elif self.version[:3] == '5.1':
            text = (
                'Future version compatible with PHP 7.1 and newer and MySQL 5.5 and newer. '
            )
        elif self.version[:3] == '5.0':
            text = (
                'Current version compatible with PHP 7.1 and newer and MySQL 5.5 and newer. '
            )
        elif self.version[:3] == '4.9':
            text = (
                'Older version compatible with PHP 5.5 to 7.4 and MySQL 5.5 and newer. ' +
                'Currently supported for security fixes only. '
            )
        elif self.version[:3] == '4.8':
            text = (
                'Older version compatible with PHP 5.5 to 7.2 and MySQL 5.5 and newer. ' +
                'Was supported until June 4, 2019.'
            )
        elif self.version in ('4.7.0', '4.7.1', '4.7.2', '4.7.3', '4.7.0-rc1', '4.7.0-beta1'):
            text = (
                'Older version compatible with PHP 5.5 to 7.1 and MySQL 5.5 and newer. ' +
                'Was supported until April 7, 2018.'
            )
        elif self.version[:3] == '4.7':
            text = (
                'Older version compatible with PHP 5.5 to 7.2 and MySQL 5.5 and newer. ' +
                'Was supported until April 7, 2018.'
            )
        elif self.version[:3] == '4.6':
            text = (
                'Older version compatible with PHP 5.5 to 7.1 and MySQL 5.5 and newer. ' +
                'Was supported until April 1, 2017.'
            )
        elif self.version[:3] == '4.5':
            text = (
                'Older version compatible with PHP 5.5 to 7.0 and MySQL 5.5. ' +
                'Was supported until April 1, 2016.'
            )
        elif self.version[:3] == '4.4':
            text = (
                'Older version compatible with PHP 5.3.7 to 7.0 and MySQL 5.5. ' +
                'Was supported until October 1, 2016.'
            )
        elif self.version[:3] == '4.3':
            text = (
                'Older version compatible with PHP 5.3 and MySQL 5.5. ' +
                'Was supported until October 1, 2015.'
            )
        elif self.version[:3] == '4.2':
            text = (
                'Older version compatible with PHP 5.3 and MySQL 5.5. ' +
                'Was supported until July 1, 2015.'
            )
        elif self.version[:3] == '4.1':
            text = (
                'Older version compatible with PHP 5.3 and MySQL 5.5. ' +
                'Was supported until January 1, 2015.'
            )
        elif self.version[:3] == '4.0':
            text = (
                'Older version compatible with PHP 5.2 and MySQL 5. ' +
                'Does not support PHP 5.5 or newer. ' +
                'Was supported until April 1, 2017.'
            )
        text += self.get_version_suffix()

        return text

    def get_downloads(self):
        """Lists downloads, making all-languages.zip first"""
        dlset = self.download_set
        return (
            list(dlset.filter(filename__endswith='all-languages.zip')) +
            list(dlset.exclude(filename__endswith='all-languages.zip'))
        )


class Download(models.Model):
    release = models.ForeignKey(Release)
    filename = models.CharField(max_length=50)
    size = models.IntegerField(default=0)
    sha1 = models.CharField(max_length=40)
    sha256 = models.CharField(max_length=64)
    signed = models.BooleanField(default=False)

    class Meta(object):
        ordering = ['-release__version_num', 'filename']
        unique_together = ['release', 'filename']

    def __unicode__(self):
        if self.release.snapshot:
            return '/snapshots/{0}'.format(
                self.filename
            )
        return '/phpMyAdmin/{0}/{1}'.format(
            self.release.version,
            self.filename
        )

    @property
    def size_k(self):
        return self.size / 1024

    @property
    def size_m(self):
        return self.size / (1024 * 1024)

    def get_filesystem_path(self):
        return os.path.join(
            settings.FILES_PATH,
            'phpMyAdmin',
            self.release.version,
            self.filename
        )

    def get_absolute_url(self):
        return 'https://files.phpmyadmin.net{0}'.format(
            self.__unicode__()
        )

    def get_signed_url(self):
        if not self.signed:
            return ''
        return 'https://files.phpmyadmin.net{0}.asc'.format(
            self.__unicode__()
        )

    def get_checksum_url(self):
        return 'https://files.phpmyadmin.net{0}.sha256'.format(
            self.__unicode__()
        )

    def get_alternate_url(self):
        return 'https://1126968067.rsc.cdn77.org{0}'.format(
            self.__unicode__()
        )

    @property
    def archive(self):
        return self.filename.rsplit('.', 1)[-1]

    @property
    def composer_type(self):
        ext = self.filename.rsplit('.', 1)[-1]
        if ext == 'zip':
            return 'zip'
        else:
            return 'tar'

    @property
    def get_stable_url(self):
        filename, ext = self.filename.rsplit('.', 1)
        if ext not in ('zip', '7z'):
            filename, ext2 = filename.rsplit('.', 1)
            ext = '{0}.{1}'.format(ext2, ext)
        variant = filename.split('-', 2)[2]
        return reverse(
            'latest-download',
            kwargs={
                'flavor': variant,
                'extension': '.' + ext,
            }
        )

    @property
    def get_stable_filename(self):
        return self.get_stable_url.rsplit('/', 1)[1]

    @property
    def is_featured(self):
        return self.filename.endswith('all-languages.zip')


class Theme(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    filename = models.CharField(max_length=100, unique=True)
    supported_versions = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    size = models.IntegerField(default=0)
    sha1 = models.CharField(max_length=40)
    sha256 = models.CharField(max_length=64)
    signed = models.BooleanField(default=False)
    date = models.DateTimeField(db_index=True, default=timezone.now)
    show = models.BooleanField(default=True)

    class Meta(object):
        ordering = ['name', 'version']

    def __unicode__(self):
        return u'{0} {1}'.format(self.display_name, self.version)

    @property
    def imgname(self):
        return 'images/themes/{0}.png'.format(self.name)

    def get_absolute_url(self):
        return 'https://files.phpmyadmin.net/themes/{0}/{1}/{2}'.format(
            self.name,
            self.version,
            self.filename,
        )

    def get_signed_url(self):
        if not self.signed:
            return ''
        return 'https://files.phpmyadmin.net/themes/{0}/{1}/{2}.asc'.format(
            self.name,
            self.version,
            self.filename,
        )

    def get_filesystem_path(self):
        return os.path.join(
            settings.FILES_PATH,
            'themes',
            self.name,
            self.version,
            self.filename
        )

    @property
    def get_css(self):
        return CSSMAP[self.supported_versions]


def dockerhub_trigger(tag):
    if settings.DOCKERHUB_TOKEN is None:
        return
    request = urllib2.Request(
        DOCKER_TRIGGER.format(settings.DOCKERHUB_TOKEN),
        json.dumps({'docker_tag': tag}),
        {'Content-Type': 'application/json'}
    )
    handle = urllib2.urlopen(request)
    handle.read()


@receiver(post_save, sender=Release)
def purge_release(sender, instance, **kwargs):
    if instance.purged:
        return
    instance.purged = True
    purge_cdn(
        # Pages with _littleboxes.html
        reverse('home'),
        reverse('news'),
        # Download lists
        reverse('files'),
        reverse('feed-files'),
        reverse('downloads'),
        # Version dumps
        '/downloads/list.txt',
        '/home_page/version.txt',
        '/home_page/version.js',
        '/home_page/version.json',
        '/downloads/phpMyAdmin-latest-all-languages.tar.bz2',
        '/downloads/phpMyAdmin-latest-all-languages.tar.gz',
        '/downloads/phpMyAdmin-latest-all-languages.tar.xz',
        '/downloads/phpMyAdmin-latest-all-languages.zip',
        '/downloads/phpMyAdmin-latest-english.tar.bz2',
        '/downloads/phpMyAdmin-latest-english.tar.gz',
        '/downloads/phpMyAdmin-latest-english.tar.xz',
        '/downloads/phpMyAdmin-latest-english.zip',
        '/downloads/phpMyAdmin-latest-source.tar.xz',
        reverse('doap'),
        reverse('pad'),
        # This release
        instance.get_absolute_url(),
    )
    # Purge all pages as every page contains download link
    purge_all_cdn()


@receiver(post_save, sender=Download)
def purge_download(sender, instance, **kwargs):
    purge_release(sender, instance.release)


@receiver(post_save, sender=Theme)
def purge_theme(sender, instance, **kwargs):
    purge_cdn(reverse('themes'))
