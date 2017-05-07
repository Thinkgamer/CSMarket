#-*-coding:utf-8-*-
from django.conf.urls import url,include
from django.contrib import admin
from cyanscikit.views import index,example,doc,onedoc,oneexample

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index),
    url(r'^example/$', example),
    url(r'^oneexample/(.+)/$', oneexample),
    url(r'^doc/$', doc),
    url(r'^onedoc/(.+)/$', onedoc),
]