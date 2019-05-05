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

from django.core.management.base import BaseCommand
from django.conf import settings
from dateutil import parser
import json
import os
from glob import glob
from files.models import Release, Download
from bs4 import BeautifulSoup
from files.utils import read_sum
import codecs
from pmaweb.cdn import purge_files_cdn


def glob_downloads(prefix=''):
    return (
        glob(prefix + '*.zip') +
        glob(prefix + '*.7z') +
        glob(prefix + '*.tar.gz') +
        glob(prefix + '*.tar.bz2') +
        glob(prefix + '*.tar.xz')
    )


class Command(BaseCommand):
    help = 'Imports files from filesystem'

    def process_files(self, path, release, prefix='', force=False):
        os.chdir(path)
        for filename in glob_downloads(prefix):
            download, created = Download.objects.get_or_create(
                release=release, filename=filename
            )
            if not created and not force:
                continue
            download.release = release
            download.size = os.path.getsize(filename)
            download.sha1 = read_sum('{0}.sha1'.format(filename))
            download.sha256 = read_sum('{0}.sha256'.format(filename))
            download.signed = os.path.exists('{0}.asc'.format(filename))
            download.save()

    def process_releases(self, path):
        for version in os.listdir(path):
            if version in ('README.rst', 'index.html'):
                continue
            release, created = Release.objects.get_or_create(version=version)
            if created:
                self.stdout.write('Added {0}'.format(version))
                notes = '{0}/{1}/phpMyAdmin-{1}-notes.html'.format(
                    path, version
                )
                if os.path.exists(notes):
                    with codecs.open(notes, 'r', 'utf-8') as handle:
                        release.release_notes_markup_type = 'html'
                        release.release_notes = u'<pre>{0}</pre>'.format(
                            BeautifulSoup(
                                handle.read(),
                                'lxml',
                            ).get_text()
                        )
                        release.save()
            self.process_files(
                os.path.join(path, version),
                release
            )

    def process_snapshots(self, path):
        os.chdir(path)

        # List current versions
        versions = set([x.rsplit('.', 1)[0].split('-')[1] for x in glob('*+snapshot.json')])

        # Delete no longer present snapshots
        Release.objects.filter(snapshot=True).exclude(version__in=versions).delete()

        purge = []

        # Process versions
        for version in versions:
            metafile = os.path.join(
                path,
                'phpMyAdmin-' + version + '.json'
            )
            with open(metafile, 'r') as handle:
                metadata = json.load(handle)
            defaults = {
                'snapshot': True,
                'release_notes': metadata['commit'],
                'release_notes_markup_type': 'plain',
                'date': parser.parse(metadata['date']),
            }
            release, created = Release.objects.get_or_create(
                version=version,
                defaults=defaults,
            )
            if created:
                self.stdout.write('Added {0}'.format(version))
            else:
                modified = False
                for item in defaults:
                    if item == 'release_notes':
                        current = release.release_notes.raw
                    else:
                        current = getattr(release, item)
                    if current != defaults[item]:
                        setattr(release, item, defaults[item])
                        modified = True
                if modified:
                    self.stdout.write('Updated {0}'.format(version))
                    release.save()
            self.process_files(
                path,
                release,
                prefix='phpMyAdmin-' + version,
                force=True,
            )
            if modified:
                for download in release.download_set.all():
                    filename = download.__unicode__()
                    purge.extend([
                        filename,
                        '{}.sha1'.format(filename),
                        '{}.sha256'.format(filename),
                    ])
        if purge:
            purge_files_cdn(*purge)

    def handle(self, *args, **options):
        self.process_releases(os.path.join(settings.FILES_PATH, 'phpMyAdmin'))
        self.process_snapshots(os.path.join(settings.FILES_PATH, 'snapshots'))
