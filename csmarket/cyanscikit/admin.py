# coding: utf8
from django.contrib import admin
from cyanscikit.models import example,doc
# Register your models here.

class adminExample(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'see_num', 'service_obj','chengjiao_time',)
    search_fields = ('title', 'pub_date', 'see_num', 'service_obj','chengjiao_time',)
    list_filter = ('pub_date', 'service_obj','chengjiao_time',)
    ordering = ('-pub_date',)

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

admin.site.register(example, adminExample)

class adminDoc(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'see_num', )
    search_fields = ('title', 'pub_date', 'see_num',)
    list_filter = ('pub_date', 'see_num',)
    ordering = ('-pub_date',)

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

admin.site.register(doc, adminDoc)
