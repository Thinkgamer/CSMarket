#-*-coding:utf-8-*-
from django.conf.urls import url,include
from django.contrib import admin
from manager.views import usermanager

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usermanager/$', usermanager),
]