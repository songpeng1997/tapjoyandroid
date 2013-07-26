"""urlconf for the apps application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('apps.views',
	url(r'^home/$','home', name='apphome'),
	url(r'^search/$','search', name='appsearch'),
	url(r'^download/$','download', name='appdownload'),
	url(r'^subcategory/(?P<subcategory_id>\d+)/$', 'sub_category', name='subcategory'),
	url(r'^app/(?P<app_id>[a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12})/$', 'app_detail', name='appdetail'),
	url(r'^category/(?P<category_id>\d+)/$', 'category', name='category'),
    url(r'^$', 'home'),

)