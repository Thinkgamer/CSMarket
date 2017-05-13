#-*-coding:utf-8-*-
from django.conf.urls import url,include
from django.contrib import admin
from message.views import edit,postService,oneService,allService,Onecate,delete

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^postService/(.+)/$', postService),
    url(r'^edit/(.+)/(.+)/$', edit),
    url(r'^oneService/(.+)/(.+)/(.+)/$', oneService),
    url(r'^allService/(.+)/$', allService),
    url(r'^OneCate/(.+)/(.+)/$', Onecate),
    url(r'^delete/(.+)/(.+)/$', delete),
]