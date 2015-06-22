from django.core.management.base import BaseCommand
from django.conf import settings
import os
from glob import glob
from files.models import Release, Download
from bs4 import BeautifulSoup


def glob_downloads():
    return (
        glob('*.zip') +
        glob('*.7z') +
        glob('*.tar.gz') +
        glob('*.tar.bz2') +
        glob('*.tar.xz')
    )


def read_sum(filename):
    try:
        with open(filename, 'r') as handle:
            return handle.read().split()[0]
    except IOError:
        return ''


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
                notes = '{0}/{1}/phpMyAdmin-{1}-notes.html'.format(
                    path, version
                )
                if os.path.exists(notes):
                    with open(notes, 'r') as handle:
                        release.release_notes = BeautifulSoup(
                            handle.read()
                        ).get_text()
                        release.save()
            self.process_files(
                os.path.join(path, version),
                release
            )

    def handle(self, *args, **options):
        self.process_releases(os.path.join(settings.FILES_PATH, 'phpMyAdmin'))
