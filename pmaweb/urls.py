from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pmaweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Swekey link from our documentation
    url(
        r'auth_key',
        RedirectView.as_view(
            url='http://store.swekey.com/index.php?promo=pma'
        )
    ),

    # Test backend
    url(
        r'test/data$',
        TemplateView.as_view(
            template_name='test-data',
            content_type='text/plain'
        )

    # Compatibility redirects
    url(
        r'documentation'
        RedirectView.as_view(
            url='http://docs.phpmyadmin.net/'
        )
    ),
    url(
        r'snapshot'
        RedirectView.as_view(
            url='https://github.com/phpmyadmin/phpmyadmin/'
        )
    ),
    url(
        r'old-stuff/ChangeLogs/',
        RedirectView.as_view(
            url='https://github.com/phpmyadmin/history/tree/master/ChangeLogs'
        )
    ),

    # Admin interface
    url(r'^admin/', include(admin.site.urls)),
)
