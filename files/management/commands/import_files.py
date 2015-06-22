from django.core.management.base import BaseCommand
from django.conf import settings
import os
from files.models import Release, Download
from bs4 import BeautifulSoup


class Command(BaseCommand):
    help = 'Imports files from filesystem'

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
                        release.release_notes = BeautifulSoup(handle.read()).get_text()
                        release.save()

    def handle(self, *args, **options):
        self.process_releases(os.path.join(settings.FILES_PATH, 'phpMyAdmin'))
