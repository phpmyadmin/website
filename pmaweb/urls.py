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
