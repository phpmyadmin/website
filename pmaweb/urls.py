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

from django.conf.urls import include, url
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

# TODO: Handle custom error pages: https://github.com/phpmyadmin/website/issues/30
handler404 = 'pmaweb.views.notfound'

urlpatterns = [
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
        django.contrib.sitemaps.views.index,
        {'sitemaps': SITEMAPS},
        name='sitemap',
    ),
    url(
        r'^sitemap-(?P<section>.+)\.xml$',
        django.contrib.sitemaps.views.sitemap,
        {'sitemaps': SITEMAPS},
        name='django.contrib.sitemaps.views.sitemap',
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
        r'^news/(?P<page>[0-9]+)/$',
        PostArchive.as_view(),
        name='news-page'
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
        r'^security/PMASA-(?P<year>20[0-9][0-9])-(?P<sequence>[0-9]+)/draft/$',
        PMASADraftView.as_view(),
        name='security-issue-draft'
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
        r'^contractor/$',
        PMAView.as_view(
            template_name='contractor.html',
            title='Work for us',
        ),
        name='contractor'
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
        r'^sponsors/subscribe/$',
        PMAView.as_view(
            template_name='sponsors-subscribe.html',
            title='Subscribe to sponsorship',
        ),
        name='sponsors-subscribe'
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
            pattern_name='home',
            permanent=True,
        )
    ),

    # favicon.ico
    url(
        r'^(?:home_page/)favicon\.ico$',
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
        r'^(home_page/)?(latest|version)\.(php|txt)$',
        TemplateView.as_view(
            template_name='version/version.txt',
            content_type='text/plain'
        )
    ),
    url(
        r'^downloads/list\.txt$',
        TemplateView.as_view(
            template_name='version/list.txt',
            content_type='text/plain'
        )
    ),
    url(
        r'^downloads/phpMyAdmin-latest-'
        r'(?P<flavor>all-languages|english)'
        r'(?P<extension>\.zip|\.tar\.gz|\.tar\.xz|\.7z|\.tar\.bz2)'
        r'(?P<checksum>\.asc|\.sha256)?$',
        latest_download,
        name='latest-download'
    ),
    url(
        r'^downloads/phpMyAdmin-latest-'
        r'(?P<flavor>source)'
        r'(?P<extension>\.tar\.xz)'
        r'(?P<checksum>\.asc|\.sha256)?$',
        latest_download,
        name='latest-download'
    ),
    url(
        r'^(home_page/)?version\.js$',
        TemplateView.as_view(
            template_name='version/version.js',
            content_type='application/javascript'
        )
    ),
    url(
        r'^(?:home_page/)?version\.json$',
        version_json,
    ),

    # GiHub API proxy
    url(
        r'^api/commit/(?P<name>[a-f0-9]{40})/',
        github_commit,
    ),
    url(
        r'^api/tree/(?P<name>[a-zA-Z0-9_]*)/',
        github_tree,
    ),


    # Composer packages
    url(
        r'^packages\.json$',
        TemplateView.as_view(
            template_name='version/packages.json',
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
        r'^(?:documentation/changelog.php|[cC]hange[Ll]og.txt|ANNOUNCE.txt)',
        RedirectView.as_view(
            url='https://demo.phpmyadmin.net/master-config/index.php?route=/changelog',
            permanent=True,
        )
    ),
    url(
        r'^documentation/scripts/setup.php$',
        RedirectView.as_view(
            url='https://demo.phpmyadmin.net/master-config/setup/',
            permanent=True,
        )
    ),
    url(
        r'^phpdoc',
        RedirectView.as_view(
            url='https://develdocs.phpmyadmin.net/',
            permanent=True,
        )
    ),
    url(
        r'^(?:phpMyAdmin/)?Documentation.html$',
        RedirectView.as_view(
            url='https://docs.phpmyadmin.net/',
            permanent=True,
        )
    ),
    url(
        r'^(?:documentation|pma_localized_docs|localized_|manual/)',
        RedirectView.as_view(
            url='https://docs.phpmyadmin.net/',
            permanent=True,
        )
    ),
    url(
        r'^(?:snapshot|cvs)',
        RedirectView.as_view(
            url='https://github.com/phpmyadmin/phpmyadmin/',
            permanent=True,
        )
    ),
    url(
        r'^old-stuff/$',
        RedirectView.as_view(
            url='https://github.com/phpmyadmin/history',
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
        r'^home[_ ]?page/' +
        r'(?:security/PMASA|security/pmasa|\.\.\.ASA)-'
        r'(?P<year>20[0-9][0-9])-(?P<sequence>[0-9]+)\)?(\.php.*)?$',
        RedirectView.as_view(
            pattern_name='security-issue',
            permanent=True,
        )
    ),
    url(
        r'^home[_ ]?page/security\.php$',
        redirect_security,
    ),
    url(
        r'^home[_ ]?page/$',
        RedirectView.as_view(
            pattern_name='home',
            permanent=True,
        )
    ),
    url(
        r'^search/$',
        RedirectView.as_view(
            pattern_name='home',
            permanent=True,
        )
    ),
    url(
        r'^home_page/sitemap\.xml$',
        RedirectView.as_view(
            pattern_name='sitemap',
            permanent=True,
        )
    ),
    url(
        r'^home[_ /]?page/(?P<page>[a-z0-9-]*)\.php(.*)?$',
        redirect_home_page,
    ),
    url(
        r'gophp5',
        RedirectView.as_view(
            pattern_name='home',
            permanent=True,
        )
    ),
    url(
        r'cgi-bin/mailman/listinfo/mailman',
        RedirectView.as_view(
            url='https://lists.phpmyadmin.net/',
            permanent=True,
        )
    ),
    # Some weird URLs seen in wild
    url(
        r'^news/&.*',
        RedirectView.as_view(
            pattern_name='news',
            permanent=True,
        )
    ),
    url(
        r'^(?:download|files/\*/|downloads/\.PhpMyAdmin)$',
        RedirectView.as_view(
            pattern_name='download',
            permanent=True,
        )
    ),
    url(
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
    url(r'^admin/', include(admin.site.urls)),
]
