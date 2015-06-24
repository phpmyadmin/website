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

from django.core.management.base import BaseCommand
from django.conf import settings
import os
from glob import glob
from files.models import Release, Download
from bs4 import BeautifulSoup
from files.utils import read_sum


def glob_downloads():
    return (
        glob('*.zip') +
        glob('*.7z') +
        glob('*.tar.gz') +
        glob('*.tar.bz2') +
        glob('*.tar.xz')
    )


class Command(BaseCommand):
    help = 'Imports files from filesystem'

    def process_files(self, path, release):
        os.chdir(path)
        for filename in glob_downloads():
            download, created = Download.objects.get_or_create(
                release=release, filename=filename
            )
            if not created:
                continue
            download.size = os.path.getsize(filename)
            download.sha1 = read_sum('{0}.sha1'.format(filename))
            download.md5 = read_sum('{0}.md5'.format(filename))
            download.signed = os.path.exists('{0}.asc'.format(filename))
            download.save()

    def process_releases(self, path):
        for version in os.listdir(path):
            if version == 'README.rst':
                continue
            release, created = Release.objects.get_or_create(version=version)
            if created:
                self.stdout.write('Added {0}'.format(version))
                notes = '{0}/{1}/phpMyAdmin-{1}-notes.html'.format(
                    path, version
                )
                if os.path.exists(notes):
                    with open(notes, 'r') as handle:
                        release.release_notes_markup_type = 'html'
                        release.release_notes = '<pre>{0}</pre>'.format(
                            BeautifulSoup(
                                handle.read()
                            ).get_text()
                        )
                        release.save()
            self.process_files(
                os.path.join(path, version),
                release
            )

    def handle(self, *args, **options):
        self.process_releases(os.path.join(settings.FILES_PATH, 'phpMyAdmin'))
