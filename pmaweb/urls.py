from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pmaweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

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
        r'^improve/$',
        TemplateView.as_view(
            template_name='improve.html',
        ),
        name='improve'
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

    # Admin interface
    url(r'^admin/', include(admin.site.urls)),
)
