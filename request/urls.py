from django.conf.urls import patterns, url

from request import views

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^name/$', name),
)
