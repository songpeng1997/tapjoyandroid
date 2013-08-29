"""urlconf for the apps application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('apps.views',
	
	url(r'^search/$','search', name='appsearch'),
	url(r'^download/$','download', name='appdownload'),
	url(r'^subcategory/(?P<subcategory_id>\d+)/$', 'sub_category', name='subcategory'),
	url(r'^subcategory/(?P<subcategory_id>\d+)/(?P<page>\d+)/$', 'subcategory_app_list', name='subcategory_app_list'),
	url(r'^app/(?P<app_id>[a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12})/$', 'app_detail', name='appdetail'),
	url(r'^category/(?P<category_id>\d+)/$', 'category', name='category'),
	url(r'^category/(?P<category_id>\d+)/(?P<page>\d+)/$', 'category_app_list', name='category_app_list'),
    url(r'^$', 'home', name = 'appsbase'),
    url(r'^home/$','home', name='apphome'),
    url(r'^home/(?P<page>\d+)/$', 'home_recomm_list', name='home_recomm_list'),

)