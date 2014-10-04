from django.conf.urls import patterns, include, url
from request import views
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'get_name', views.get_name),
)
