from django.core.management.base import BaseCommand
from django.conf import settings
from files.models import Release


class Command(BaseCommand):
    help = 'Ranks releases to be shown'

    def handle(self, *args, **options):
        index = 0
        latest = beta = Release.objects.all()[0]
        if beta.version_num % 100 == 99:
            beta = None

        while latest.version_num % 100 != 99:
            index += 1
            latest = Release.objects.all()[1]

        print 'BETA', beta
        print 'LATEST', latest

        delta = 1000000

        for version in settings.LISTED_BRANCHES:
            min_vernum = Release.parse_version(version)
            max_vernum = min_vernum + delta
            print Release.objects.filter(
                version_num__gte=min_vernum,
                version_num__lt=max_vernum,
            )[0]
