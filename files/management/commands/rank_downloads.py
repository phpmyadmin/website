from django.core.management.base import BaseCommand
from django.conf import settings
from files.models import Release
from pmaweb.context_processors import releases


class Command(BaseCommand):
    help = 'Ranks releases to be shown'

    def handle(self, *args, **options):
        data = releases()

        self.stdout.write('Latest: {0}'.format(data['latest']))
        if data['beta']:
            self.stdout.write('Beta: {0}'.format(data['beta']))

        self.stdout.write('')

        self.stdout.write('Releases:')
        for release in data['releases']:
            self.stdout.write(' * {0}'.format(release))
