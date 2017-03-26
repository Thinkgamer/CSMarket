"""csmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from csmarket.views import index
from csmarket.upload import upload_image
from django import views
from django.conf import settings

urlpatterns = [
    #url(r'^admin/uploads/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    #url(r"^uploads/(?P<path>.*)$", views.static.serve, {"document_root": settings.MEDIA_ROOT, }),

    url(r'^admin/', admin.site.urls),
    url(r'^logre/', include('logre.urls')),
    url(r'^manager/', include('manager.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^message/', include('message.urls')),
    url(r'^index/', index),
    url(r'^$', index),
]
