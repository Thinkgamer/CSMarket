#-*-coding:utf-8-*-
from django.conf.urls import url,include
from django.contrib import admin
from logre.views import login,register,prefect

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^register/$', register),
    url(r'^prefect/$', prefect),
]