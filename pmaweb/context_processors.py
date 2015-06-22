from files.models import Release
from news.models import Post
from django.conf import settings
from django.core.urlresolvers import reverse
import datetime

from data.menu import MENU
from data.screenshots import SCREENSHOTS


def basic(request):
    return {
        'current_year': datetime.datetime.now().year,
        'short_news': Post.objects.all()[:5],
        'screenshots': SCREENSHOTS,
    }


def menu(request):
    result = []

    for name, title in MENU:
        if name:
            urlname = name.rstrip('/')
        else:
            urlname = 'home'

        result.append({
            'title': title,
            'url': reverse(urlname),
            'active': urlname == request.resolver_match.url_name,
        })

    return {
        'menu': result,
    }


def releases(request=None):

    latest = Release.objects.filter(stable=True)[0]
    beta = Release.objects.filter(stable=False)[0]
    if beta.version_num < latest.version_num:
        beta = None

    delta = 1000000
    releases = []

    for version in settings.LISTED_BRANCHES:
        min_vernum = Release.parse_version(version)
        max_vernum = min_vernum + delta
        releases.append(Release.objects.filter(
            version_num__gte=min_vernum,
            version_num__lt=max_vernum,
            stable=True,
        )[0])

    return {
        'latest': latest,
        'beta': beta,
        'releases': releases,
    }
