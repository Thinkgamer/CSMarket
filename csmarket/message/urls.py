#-*-coding:utf-8-*-
from django.conf.urls import url,include
from django.contrib import admin
from message.views import editService,postService,oneService,allService

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^postService/(.+)/$', postService),
    url(r'^editService/(.+)/$', editService),
    url(r'^oneService/(.+)/(.+)/$', oneService),
    url(r'^allService/(.+)/$', allService),
]