""" Default urlconf for tapjoyandroid """

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
                       url(r'^huadmin/doc/', include(
                           'django.contrib.admindocs.urls')),
                       url(r'^huadmin/$', admin.site.admin_view(
                           admin.site.index)),
                       url(r'^huadmin/', include(admin.site.urls)),
                       #url(r'^', include('debug_toolbar_user_panel.urls')),
                       url(r'^bad/$', bad),
                       url(r'^apps/', include('apps.urls')),
                       url(r'^m/', include('apps.urls')),
                       url(r'', include('base.urls')),
                       )

# In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
                           (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT}),
                            )
