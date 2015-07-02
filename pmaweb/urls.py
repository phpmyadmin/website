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

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from pmaweb.views import PMAView
from security.views import PMASAView
from files.views import ReleaseList, ReleaseDetail
from news.views import PostArchive, PostDetail
from news.feeds import NewsFeed
from files.feeds import ReleaseFeed
from security.feeds import PMASAFeed
from pmaweb.sitemaps import SITEMAPS


TRANSLATIONS_RSS = 'https://hosted.weblate.org/exports/rss/phpmyadmin/'

handler404 = 'pmaweb.views.notfound'

urlpatterns = patterns(
    '',
    # Feeds
    url(
        r'news/feed/$',
        NewsFeed(),
        name='feed-news',
    ),
    url(
        r'files/feed/$',
        ReleaseFeed(),
        name='feed-files',
    ),
    url(
        r'security/feed/$',
        PMASAFeed(),
        name='feed-security',
    ),

    # XML sitemap
    url(
        r'^sitemap.xml$',
        'django.contrib.sitemaps.views.index',
        {'sitemaps': SITEMAPS}
    ),
    url(
        r'^sitemap-(?P<section>.+)\.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': SITEMAPS}
    ),

    # Pages
    url(
        r'^$',
        PMAView.as_view(
            template_name='index.html',
        ),
        name='home'
    ),
    url(
        r'^news/$',
        PostArchive.as_view(),
        name='news'
    ),
    url(
        r'^news/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[^/]+)/$',
        PostDetail.as_view(),
        name='news-item'
    ),
    url(
        r'^security/$',
        PMAView.as_view(
            template_name='security/index.html',
            title='Security',
            rss='feed-security',
            rss_title='phpMyAdmin security announcements',
        ),
        name='security'
    ),
    url(
        r'^security/PMASA-(?P<year>20[0-9][0-9])-(?P<sequence>[0-9]+)/$',
        PMASAView.as_view(),
        name='security-issue'
    ),
    url(
        r'^support/$',
        PMAView.as_view(
            template_name='support.html',
            title='Support',
        ),
        name='support'
    ),
    url(
        r'^docs/$',
        PMAView.as_view(
            template_name='docs.html',
            title='Documentation',
        ),
        name='docs'
    ),
    url(
        r'^try/$',
        PMAView.as_view(
            template_name='try.html',
            title='Try',

        ),
        name='try'
    ),
    url(
        r'^contribute/$',
        PMAView.as_view(
            template_name='contribute.html',
            title='Contribute',
        ),
        name='contribute'
    ),
    url(
        r'^sponsors/$',
        PMAView.as_view(
            template_name='sponsors.html',
            title='Sponsors',
        ),
        name='sponsors'
    ),
    url(
        r'^themes/$',
        PMAView.as_view(
            template_name='themes.html',
            title='Themes',
        ),
        name='themes'
    ),
    url(
        r'^license/$',
        PMAView.as_view(
            template_name='license.html',
            title='License',
        ),
        name='license'
    ),
    url(
        r'^team/$',
        PMAView.as_view(
            template_name='team.html',
            title='Team',
        ),
        name='team'
    ),
    url(
        r'^translations/$',
        PMAView.as_view(
            template_name='translations.html',
            title='Translations',
            rss=TRANSLATIONS_RSS,
            rss_title='phpMyAdmin translation changes',
        ),
        name='translations'
    ),
    url(
        r'^awards/$',
        PMAView.as_view(
            template_name='awards.html',
            title='Awards',
        ),
        name='awards'
    ),
    url(
        r'^about/$',
        PMAView.as_view(
            template_name='about.html',
            title='About',
        ),
        name='about'
    ),
    url(
        r'^15-years/$',
        PMAView.as_view(
            template_name='15-years.html',
            title='15 years',
        ),
        name='15-years'
    ),
    url(
        r'^donate/$',
        PMAView.as_view(
            template_name='donate.html',
            title='Donate',
        ),
        name='donate'
    ),
    url(
        r'^search/$',
        PMAView.as_view(
            template_name='search.html',
            title='Search',
        ),
        name='search'
    ),
    url(
        r'^about-website/$',
        PMAView.as_view(
            template_name='about-website.html',
            title='About website',
        ),
        name='about-website'
    ),
    url(
        r'^downloads/$',
        PMAView.as_view(
            template_name='downloads.html',
            title='Downloads',
            rss='feed-files',
            rss_title='phpMyAdmin releases',
        ),
        name='downloads'
    ),
    url(
        r'^translate/$',
        PMAView.as_view(
            template_name='translate.html',
            title='Translating',
            rss=TRANSLATIONS_RSS,
            rss_title='phpMyAdmin translation changes',
        ),
        name='translate'
    ),
    url(
        r'^develop/$',
        PMAView.as_view(
            template_name='develop.html',
            title='Developing',
        ),
        name='develop'
    ),
    url(
        r'^contest/$',
        PMAView.as_view(
            template_name='contest.html',
            title='Contest',
        ),
        name='contest'
    ),
    url(
        r'^files/$',
        ReleaseList.as_view(),
        name='files'
    ),
    url(
        r'^files/(?P<version>[a-z0-9.-]*)/$',
        ReleaseDetail.as_view(),
        name='release'
    ),

    # Swekey link from our documentation
    url(
        r'auth_key',
        RedirectView.as_view(
            url='http://store.swekey.com/index.php?promo=pma',
            permanent=False,
        )
    ),

    # favicon.ico
    url(
        r'^favicon\.ico$',
        RedirectView.as_view(
            url='/static/favicon.ico',
            permanent=True,
        )
    ),

    # robots.txt
    url(
        r'^robots.txt$',
        TemplateView.as_view(
            template_name='robots.txt',
            content_type='text/plain'
        )
    ),

    # Machine parsable output
    url(
        r'^home_page/phpmyadmin.xml$',
        TemplateView.as_view(
            template_name='phpmyadmin.xml',
            content_type='application/xml'
        ),
        name='pad',
    ),
    url(
        r'^home_page/phpmyadmin-doap.xml$',
        TemplateView.as_view(
            template_name='phpmyadmin-doap.xml',
            content_type='application/xml'
        ),
        name='doap',
    ),

    # Version information
    url(
        r'^(home_page/)?version\.(php|txt)$',
        TemplateView.as_view(
            template_name='version/version.txt',
            content_type='text/plain'
        )
    ),
    url(
        r'^(home_page/)?version\.js$',
        TemplateView.as_view(
            template_name='version/version.js',
            content_type='application/javascript'
        )
    ),
    url(
        r'^(home_page/)?version\.json$',
        TemplateView.as_view(
            template_name='version/version.json',
            content_type='application/json'
        )
    ),

    # Test backend
    url(
        r'^test/data$',
        TemplateView.as_view(
            template_name='test-data',
            content_type='text/plain'
        )
    ),

    # Compatibility redirects
    url(
        r'^documentation/changelog.php$',
        RedirectView.as_view(
            url='http://demo.phpmyadmin.net/master-config/changelog.php',
            permanent=True,
        )
    ),
    url(
        r'^phpdoc',
        RedirectView.as_view(
            url='http://docs.phpmyadmin.net/',
            permanent=True,
        )
    ),
    url(
        r'^documentation',
        RedirectView.as_view(
            url='http://docs.phpmyadmin.net/',
            permanent=True,
        )
    ),
    url(
        r'^snapshot',
        RedirectView.as_view(
            url='https://github.com/phpmyadmin/phpmyadmin/',
            permanent=True,
        )
    ),
    url(
        r'^old-stuff/ChangeLogs/',
        RedirectView.as_view(
            url='https://github.com/phpmyadmin/history/tree/master/ChangeLogs',
            permanent=True,
        )
    ),
    url(
        r'^home_page/security/(?:index.php)?$',
        RedirectView.as_view(
            pattern_name='security',
            permanent=True,
        )
    ),
    url(
        r'^home_page/security/index.xml$',
        RedirectView.as_view(
            pattern_name='feed-security',
            permanent=True,
        )
    ),
    url(
        r'^home_page/security/' +
        r'PMASA-(?P<year>20[0-9][0-9])-(?P<sequence>[0-9]+)\.php$',
        RedirectView.as_view(
            pattern_name='security-issue',
            permanent=True,
        )
    ),
    url(
        r'^home_page/security\.php$',
        'pmaweb.views.redirect_security',
    ),
    url(
        r'^home_page/$',
        RedirectView.as_view(
            pattern_name='home',
            permanent=True,
        )
    ),
    url(
        r'^home_page/(?P<page>[a-z0-9-]*)\.php$',
        'pmaweb.views.redirect_home_page',
    ),

    # Admin interface
    url(r'^admin/', include(admin.site.urls)),
)
