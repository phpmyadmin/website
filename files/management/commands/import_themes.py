from django.core.management.base import BaseCommand
from django.conf import settings
import os
from files.models import Theme
from data.themes import THEMES


class Command(BaseCommand):
    help = 'Imports themes from filesystem'

    def process_theme(self, path, fullname):
        name, version, filename = fullname.split('/')
        namever = os.path.splitext(filename)[0]
        try:
            data = THEMES[namever]
        except KeyError:
            self.stderr.write('Unknown theme: {0}'.format(namever))
            return

        Theme.objects.get_or_create(
            filename=filename,
            name=name,
            version=version,
            defaults={
                'size': os.path.getsize(os.path.join(path, fullname)),
                'display_name': data['name'],
                'supported_versions': data['support'],
                'description': data['info'],
                'author': data['author'],
            }
        )

    def handle(self, *args, **options):
        path = os.path.join(settings.FILES_PATH, 'themes')
        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.endswith(".zip"):
                    fullname = os.path.join(
                        root[len(path):].lstrip('/'), filename
                    )
                    self.process_theme(path, fullname)
