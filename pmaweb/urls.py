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

from django.urls import path, re_path
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from pmaweb.views import PMAView, redirect_home_page, github_tree, github_commit
from security.views import PMASAView, PMASADraftView, redirect_security
from files.views import (
    ReleaseList, ReleaseDetail, version_json, latest_download
)
from news.views import PostArchive, PostDetail
from news.feeds import NewsFeed
from files.feeds import ReleaseFeed
from security.feeds import PMASAFeed
from pmaweb.sitemaps import SITEMAPS
import django.contrib.sitemaps.views


TRANSLATIONS_RSS = 'https://hosted.weblate.org/exports/rss/phpmyadmin/'

handler404 = 'pmaweb.views.notfound'

urlpatterns = [
    # Feeds
    path(
        'news/feed/',
        NewsFeed(),
        name='feed-news',
    ),
    path(
        'files/feed/',
        ReleaseFeed(),
        name='feed-files',
    ),
    path(
        'security/feed/',
        PMASAFeed(),
        name='feed-security',
    ),

    # XML sitemap
    path(
        'sitemap.xml',
        django.contrib.sitemaps.views.index,
        {'sitemaps': SITEMAPS},
        name='sitemap',
    ),
    path(
        'sitemap-<path:section>.xml',
        django.contrib.sitemaps.views.sitemap,
        {'sitemaps': SITEMAPS},
        name='django.contrib.sitemaps.views.sitemap',
    ),

    # Pages
    path(
        '',
        PMAView.as_view(
            template_name='index.html',
        ),
        name='home'
    ),
    path(
        'news/',
        PostArchive.as_view(),
        name='news'
    ),
    path(
        'news/<int:page>/',
        PostArchive.as_view(),
        name='news-page'
    ),
    path(
        'news/<int:year>/<int:month>/<int:day>/<str:slug>/',
        PostDetail.as_view(),
        name='news-item'
    ),
    path(
        'security/',
        PMAView.as_view(
            template_name='security/index.html',
            title='Security',
            rss='feed-security',
            rss_title='phpMyAdmin security announcements',
        ),
        name='security'
    ),
    re_path(
        r'^security/PMASA-(?P<year>20[0-9][0-9])-(?P<sequence>[0-9]+)/$',
        PMASAView.as_view(),
        name='security-issue'
    ),
    re_path(
        r'^security/PMASA-(?P<year>20[0-9][0-9])-(?P<sequence>[0-9]+)/draft/$',
        PMASADraftView.as_view(),
        name='security-issue-draft'
    ),
    path(
        'support/',
        PMAView.as_view(
            template_name='support.html',
            title='Support',
        ),
        name='support'
    ),
    path(
        'docs/',
        PMAView.as_view(
            template_name='docs.html',
            title='Documentation',
        ),
        name='docs'
    ),
    path(
        'try/',
        PMAView.as_view(
            template_name='try.html',
            title='Try',

        ),
        name='try'
    ),
    path(
        'contribute/',
        PMAView.as_view(
            template_name='contribute.html',
            title='Contribute',
        ),
        name='contribute'
    ),
    path(
        'contractor/',
        PMAView.as_view(
            template_name='contractor.html',
            title='Work for us',
        ),
        name='contractor'
    ),
    path(
        'sponsors/',
        PMAView.as_view(
            template_name='sponsors.html',
            title='Sponsors',
        ),
        name='sponsors'
    ),
    path(
        'sponsors/subscribe/',
        PMAView.as_view(
            template_name='sponsors-subscribe.html',
            title='Subscribe to sponsorship',
        ),
        name='sponsors-subscribe'
    ),
    path(
        'themes/',
        PMAView.as_view(
            template_name='themes.html',
            title='Themes',
        ),
        name='themes'
    ),
    path(
        'license/',
        PMAView.as_view(
            template_name='license.html',
            title='License',
        ),
        name='license'
    ),
    path(
        'team/',
        PMAView.as_view(
            template_name='team.html',
            title='Team',
        ),
        name='team'
    ),
    path(
        'translations/',
        PMAView.as_view(
            template_name='translations.html',
            title='Translations',
            rss=TRANSLATIONS_RSS,
            rss_title='phpMyAdmin translation changes',
        ),
        name='translations'
    ),
    path(
        'awards/',
        PMAView.as_view(
            template_name='awards.html',
            title='Awards',
        ),
        name='awards'
    ),
    path(
        'about/',
        PMAView.as_view(
            template_name='about.html',
            title='About',
        ),
        name='about'
    ),
    path(
        '15-years/',
        PMAView.as_view(
            template_name='15-years.html',
            title='15 years',
        ),
        name='15-years'
    ),
    path(
        'donate/',
        PMAView.as_view(
            template_name='donate.html',
            title='Donate',
        ),
        name='donate'
    ),
    path(
        'about-website/',
        PMAView.as_view(
            template_name='about-website.html',
            title='About website',
        ),
        name='about-website'
    ),
    path(
        'downloads/',
        PMAView.as_view(
            template_name='downloads.html',
            title='Downloads',
            rss='feed-files',
            rss_title='phpMyAdmin releases',
        ),
        name='downloads'
    ),
    path(
        'translate/',
        PMAView.as_view(
            template_name='translate.html',
            title='Translating',
            rss=TRANSLATIONS_RSS,
            rss_title='phpMyAdmin translation changes',
        ),
        name='translate'
    ),
    path(
        'develop/',
        PMAView.as_view(
            template_name='develop.html',
            title='Developing',
        ),
        name='develop'
    ),
    path(
        'contest/',
        PMAView.as_view(
            template_name='contest.html',
            title='Contest',
        ),
        name='contest'
    ),
    path(
        'files/',
        ReleaseList.as_view(),
        name='files'
    ),
    re_path(
        r'^files/(?P<version>[a-z0-9.-]*)/$',
        ReleaseDetail.as_view(),
        name='release'
    ),

    # Swekey link from our documentation
    re_path(
        r'auth_key',
        RedirectView.as_view(
            pattern_name='home',
            permanent=True,
        )
    ),

    # favicon.ico
    re_path(
        r'^(?:home_page/)favicon\.ico$',
        RedirectView.as_view(
            url='/static/favicon.ico',
            permanent=True,
        )
    ),

    # robots.txt
    path(
        'robots.txt',
        TemplateView.as_view(
            template_name='robots.txt',
            content_type='text/plain'
        )
    ),

    # Machine parsable output
    path(
        'home_page/phpmyadmin.xml',
        TemplateView.as_view(
            template_name='phpmyadmin.xml',
            content_type='application/xml'
        ),
        name='pad',
    ),
    path(
        'home_page/phpmyadmin-doap.xml',
        TemplateView.as_view(
            template_name='phpmyadmin-doap.xml',
            content_type='application/xml'
        ),
        name='doap',
    ),

    # Version information
    re_path(
        r'^(home_page/)?(latest|version)\.(php|txt)$',
        TemplateView.as_view(
            template_name='version/version.txt',
            content_type='text/plain'
        )
    ),
    path(
        'downloads/list.txt',
        TemplateView.as_view(
            template_name='version/list.txt',
            content_type='text/plain'
        )
    ),
    re_path(
        r'^downloads/phpMyAdmin-latest-'
        r'(?P<flavor>all-languages|english)'
        r'(?P<extension>\.zip|\.tar\.gz|\.tar\.xz|\.7z|\.tar\.bz2)'
        r'(?P<checksum>\.asc|\.sha256)?$',
        latest_download,
        name='latest-download'
    ),
    re_path(
        r'^downloads/phpMyAdmin-latest-'
        r'(?P<flavor>source)'
        r'(?P<extension>\.tar\.xz)'
        r'(?P<checksum>\.asc|\.sha256)?$',
        latest_download,
        name='latest-download'
    ),
    re_path(
        r'^(home_page/)?version\.js$',
        TemplateView.as_view(
            template_name='version/version.js',
            content_type='application/javascript'
        )
    ),
    re_path(
        r'^(?:home_page/)?version\.json$',
        version_json,
    ),

    # GiHub API proxy
    re_path(
        r'^api/commit/(?P<name>[a-f0-9]{40})/',
        github_commit,
    ),
    re_path(
        r'^api/tree/(?P<name>[a-zA-Z0-9_]*)/',
        github_tree,
    ),


    # Composer packages
    path(
        'packages.json',
        TemplateView.as_view(
            template_name='version/packages.json',
            content_type='application/json'
        )
    ),

    # Test backend
    path(
        'test/data',
        TemplateView.as_view(
            template_name='test-data',
            content_type='text/plain'
        )
    ),

    # Compatibility redirects
    re_path(
        r'^(?:documentation/changelog.php|[cC]hange[Ll]og.txt|ANNOUNCE.txt)',
        RedirectView.as_view(
            url='https://demo.phpmyadmin.net/master-config/index.php?route=/changelog',
            permanent=True,
        )
    ),
    path(
        'documentation/scripts/setup.php',
        RedirectView.as_view(
            url='https://demo.phpmyadmin.net/master-config/setup/',
            permanent=True,
        )
    ),
    re_path(
        r'^phpdoc',
        RedirectView.as_view(
            url='https://develdocs.phpmyadmin.net/',
            permanent=True,
        )
    ),
    re_path(
        r'^(?:phpMyAdmin/)?Documentation.html$',
        RedirectView.as_view(
            url='https://docs.phpmyadmin.net/',
            permanent=True,
        )
    ),
    re_path(
        r'^(?:documentation|pma_localized_docs|localized_|manual/)',
        RedirectView.as_view(
            url='https://docs.phpmyadmin.net/',
            permanent=True,
        )
    ),
    re_path(
        r'^(?:snapshot|cvs)',
        RedirectView.as_view(
            url='https://github.com/phpmyadmin/phpmyadmin/',
            permanent=True,
        )
    ),
    path(
        'old-stuff/',
        RedirectView.as_view(
            url='https://github.com/phpmyadmin/history',
            permanent=True,
        )
    ),
    re_path(
        r'^old-stuff/ChangeLogs/',
        RedirectView.as_view(
            url='https://github.com/phpmyadmin/history/tree/master/ChangeLogs',
            permanent=True,
        )
    ),
    re_path(
        r'^home_page/security/(?:index.php)?$',
        RedirectView.as_view(
            pattern_name='security',
            permanent=True,
        )
    ),
    path(
        'home_page/security/index.xml',
        RedirectView.as_view(
            pattern_name='feed-security',
            permanent=True,
        )
    ),
    re_path(
        r'^home[_ ]?page/' +
        r'(?:security/PMASA|security/pmasa|\.\.\.ASA)-'
        r'(?P<year>20[0-9][0-9])-(?P<sequence>[0-9]+)\)?(\.php.*)?$',
        RedirectView.as_view(
            pattern_name='security-issue',
            permanent=True,
        )
    ),
    re_path(
        r'^home[_ ]?page/security\.php$',
        redirect_security,
    ),
    re_path(
        r'^home[_ ]?page/$',
        RedirectView.as_view(
            pattern_name='home',
            permanent=True,
        )
    ),
    path(
        'search/',
        RedirectView.as_view(
            pattern_name='home',
            permanent=True,
        )
    ),
    path(
        'home_page/sitemap.xml',
        RedirectView.as_view(
            pattern_name='sitemap',
            permanent=True,
        )
    ),
    re_path(
        r'^home[_ /]?page/(?P<page>[a-z0-9-]*)\.php(.*)?$',
        redirect_home_page,
    ),
    re_path(
        r'gophp5',
        RedirectView.as_view(
            pattern_name='home',
            permanent=True,
        )
    ),
    re_path(
        r'cgi-bin/mailman/listinfo/mailman',
        RedirectView.as_view(
            url='https://lists.phpmyadmin.net/',
            permanent=True,
        )
    ),
    # Some weird URLs seen in wild
    re_path(
        r'^news/&.*',
        RedirectView.as_view(
            pattern_name='news',
            permanent=True,
        )
    ),
    re_path(
        r'^(?:download|files/\*/|downloads/\.PhpMyAdmin)$',
        RedirectView.as_view(
            pattern_name='download',
            permanent=True,
        )
    ),
    re_path(
        r'^(?:https?://www\.phpmyadmin\.net/|index\.html|' +
        r'logout|auth|login|auth_|auth%5C_key|' +
        r'SignonURL.*|logoutURL.*|' +
        r'default\.htm|home|\&lang=en.*|phpMyAdmin.*|[0-9.]+)$',
        RedirectView.as_view(
            pattern_name='home',
            permanent=True,
        )
    ),

    # Admin interface
    re_path(r'^admin/', admin.site.urls),
]
