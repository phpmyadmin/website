# -*- coding: UTF-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import feedparser
from dateutil import parser
import urllib
import re
from news.models import Post

URL = 'https://sourceforge.net/p/phpmyadmin/news/feed?limit=10000'

NOTES_RE = re.compile(
    'https://(sourceforge.net/projects/phpmyadmin/files|files.phpmyadmin.net)'
    '/(phpMyAdmin/([0-9.a-z-]*)/phpMyAdmin-[0-9.a-z-]*-notes.html)(/view)?'
)

USERMAP = {
    'Marc Delisle': 'lem9',
    u'Michal Čihař': 'nijel',
}


def fixup_summary(summary):
    """Replaces sf.net URLs with our ones."""
    summary = NOTES_RE.sub('https://www.phpmyadmin.net/files/\\3/', summary)

    summary = summary.replace(
        ' rel="nofollow"', ''
    ).replace(
        'https://sourceforge.net/projects/phpmyadmin/files',
        'https://www.phpmyadmin.net/files/'
    ).replace(
        '<a href="https://sourceforge.net/project/showfiles.php?group"'
        '>https://sourceforge.net/project/showfiles.php?group</a>_id=23067',
        '<a href="https://www.phpmyadmin.net/files/">'
        'https://www.phpmyadmin.net/files/</a>'
    ).replace(
        '<a href="http://sourceforge.net/svn/?group">'
        'http://sourceforge.net/svn/?group</a>_id=23067',
        '<a href="https://github.com/phpmyadmin/">'
        'https://github.com/phpmyadmin/</a>'
    ).replace(
        '<a href="https://sourceforge.net/cvs/?group">'
        'https://sourceforge.net/cvs/?group</a>_id=23067',
        '<a href="https://github.com/phpmyadmin/">'
        'https://github.com/phpmyadmin/</a>'
    ).replace(
        'http://www.phpmyadmin.net/cvs/',
        'https://github.com/phpmyadmin/'
    ).replace(
        'http://www.phpmyadmin.net/home_page/15-years.php',
        'http://www.phpmyadmin.net/15-years/'
    )

    return summary


class Command(BaseCommand):
    help = 'Imports news from sf.net RSS feed'

    def process_feed(self, feed):
        for entry in feed.entries:

            summary = fixup_summary(entry.summary)

            Post.objects.get_or_create(
                date=parser.parse(entry.published),
                slug=slugify(entry.title),
                defaults={
                    'title': entry.title,
                    'body': summary,
                    'body_markup_type': 'html',
                    'author': User.objects.get(
                        username=USERMAP[entry.author]
                    ),
                }
            )

    def handle(self, *args, **options):
        handle = urllib.urlopen(URL)
        data = handle.read()
        parsed = feedparser.parse(data)
        if parsed.bozo == 1:
            self.stderr.write(parsed.bozo_exception)
        else:
            self.process_feed(parsed)
