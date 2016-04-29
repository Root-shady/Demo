from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns
from demo import views

urlpatterns = [
			#url(r'demo/$', views.home),
			url(r'demo/(?P<user_id>[0-9]+)/$', views.user_profile),
			url(r'demo/(?P<user_id>[0-9]+)/edit/$', views.user_edit),
			url(r'demo/login/$', views.login),
			url(r'demo/register/$', views.register),
			url(r'demo/admin/$', views.admin_all),
			url(r'demo/admin/del/(?P<user_id>[0-9]+)/$', views.admin_del),
			url(r'demo/admin/update/(?P<user_id>[0-9]+)/$', views.admin_update),
			#url(r'demo/logout/$'),
		]

urlpatterns = format_suffix_patterns(urlpatterns)
