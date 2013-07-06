"""urlconf for the apps application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('apps.views',
	url(r'^subcategory/(?P<subcategory_id>\d+)/$', 'sub_category', name='subcategroy'),
	url(r'^app/(?P<app_id>[a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12})/$', 'app_detail', name='appdetail'),
    url(r'^$', 'apps_list', name='apps_list'),

)