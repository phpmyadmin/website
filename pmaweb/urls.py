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


urlpatterns = patterns('',
    # Pages
    url(
        r'^$',
        TemplateView.as_view(
            template_name='index.html',
        ),
        name='home'
    ),
    url(
        r'^news/$',
        TemplateView.as_view(
            template_name='news.html',
        ),
        name='news'
    ),
    url(
        r'^security/$',
        TemplateView.as_view(
            template_name='security.html',
        ),
        name='security'
    ),
    url(
        r'^security/(?P<entry>PMASA-20[0-9][0-9]-[0-9]+)/$',
        # TODO: Add real view
        TemplateView.as_view(
            template_name='security.html',
        ),
        name='security-issue'
    ),
    url(
        r'^support/$',
        TemplateView.as_view(
            template_name='support.html',
        ),
        name='support'
    ),
    url(
        r'^docs/$',
        TemplateView.as_view(
            template_name='docs.html',
        ),
        name='docs'
    ),
    url(
        r'^try/$',
        TemplateView.as_view(
            template_name='try.html',
        ),
        name='try'
    ),
    url(
        r'^contribute/$',
        TemplateView.as_view(
            template_name='contribute.html',
        ),
        name='contribute'
    ),
    url(
        r'^sponsors/$',
        TemplateView.as_view(
            template_name='sponsors.html',
        ),
        name='sponsors'
    ),
    url(
        r'^themes/$',
        TemplateView.as_view(
            template_name='themes.html',
        ),
        name='themes'
    ),
    url(
        r'^license/$',
        TemplateView.as_view(
            template_name='license.html',
        ),
        name='license'
    ),
    url(
        r'^team/$',
        TemplateView.as_view(
            template_name='team.html',
        ),
        name='team'
    ),
    url(
        r'^translations/$',
        TemplateView.as_view(
            template_name='translations.html',
        ),
        name='translations'
    ),
    url(
        r'^awards/$',
        TemplateView.as_view(
            template_name='awards.html',
        ),
        name='awards'
    ),
    url(
        r'^about/$',
        TemplateView.as_view(
            template_name='about.html',
        ),
        name='about'
    ),
    url(
        r'^15-years/$',
        TemplateView.as_view(
            template_name='15-years.html',
        ),
        name='15-years'
    ),
    url(
        r'^donate/$',
        TemplateView.as_view(
            template_name='donate.html',
        ),
        name='donate'
    ),
    url(
        r'^sitemap/$',
        TemplateView.as_view(
            template_name='sitemap.html',
        ),
        name='sitemap'
    ),
    url(
        r'^search/$',
        TemplateView.as_view(
            template_name='search.html',
        ),
        name='search'
    ),
    url(
        r'^about-website/$',
        TemplateView.as_view(
            template_name='about-website.html',
        ),
        name='about-website'
    ),
    url(
        r'^downloads/$',
        TemplateView.as_view(
            template_name='downloads.html',
        ),
        name='downloads'
    ),
    url(
        r'^translate/$',
        TemplateView.as_view(
            template_name='translate.html',
        ),
        name='translate'
    ),
    url(
        r'^develop/$',
        TemplateView.as_view(
            template_name='develop.html',
        ),
        name='develop'
    ),
    url(
        r'^contest/$',
        TemplateView.as_view(
            template_name='contest.html',
        ),
        name='contest'
    ),
    url(
        r'^news/$',
        TemplateView.as_view(
            template_name='news.html',
        ),
        name='news'
    ),
    url(
        r'^news/$',
        TemplateView.as_view(
            template_name='news.html',
        ),
        name='news'
    ),

    # Swekey link from our documentation
    url(
        r'auth_key',
        RedirectView.as_view(
            url='http://store.swekey.com/index.php?promo=pma',
            permanent=False,
        )
    ),

    # TODO:
    # favicon.ico
    # robots.txt
    # version.txt
    # home_page/version.php

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
        r'^home_page/security/(?P<entry>PMASA-20[0-9][0-9]-[0-9]+).php$',
        RedirectView.as_view(
            pattern_name='security-issue',
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
