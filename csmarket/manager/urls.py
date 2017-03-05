#-*-coding:utf-8-*-
from django.conf.urls import url,include
from django.contrib import admin
from manager.views import usermanager,more,through,send,login,logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^usermanager/$', usermanager),
    url(r'^more/(\w+)/$', more),
    url(r'^through/(\w+)/$', through),
    url(r'^send/(.+)/$', send),
]