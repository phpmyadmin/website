from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pmaweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(
        r'auth_key',
        RedirectView.as_view(
            url='http://store.swekey.com/index.php?promo=pma'
        )
    ),
    url(
        r'documentation'
        RedirectView.as_view(
            url='http://docs.phpmyadmin.net/'
        )
    ),
    url(
        r'old-stuff/ChangeLogs/',
        RedirectView.as_view(
            url='https://github.com/phpmyadmin/history/tree/master/ChangeLogs'
        )
    ),
    url(r'^admin/', include(admin.site.urls)),
)
