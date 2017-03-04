#-*-coding:utf-8-*-
from django.conf.urls import url,include
from django.contrib import admin
from news.views import all,one

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^all/$', all),
    url(r'^one/$', one),
]