#-*-coding:utf-8-*-
from django.conf.urls import url,include
from django.contrib import admin
from logre.views import login,register,prefect,logout,personal

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', register),
    url(r'^prefect/$', prefect),
    url(r'^personal/$', personal),
]