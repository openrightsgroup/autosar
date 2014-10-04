from django.conf.urls import patterns, include, url
from django.contrib import admin
from request import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'autosar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', views.index),
    url(r'^request/([a-z_]+)', views.request),
)
