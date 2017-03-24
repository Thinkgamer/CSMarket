#-×-coding:utf-8-*-
from django.contrib import admin
from message.models import Cate,Message

# Register your models here.
class adminCate(admin.ModelAdmin):
    list_display = ('cate_name','cate_time','cate_num',)
    search_fields = ('cate_name','cate_time','cate_num',)
    list_filter = ('cate_name','cate_time','cate_num',)
    ordering = ('-cate_time',)

admin.site.register(Cate, adminCate)

class adminMess(admin.ModelAdmin):
    # mess_title  mess_author  mess_time  mess_cate  mess_price  mess_seenum  mess_hezuo mess_ifsuccess
    list_display = ('mess_title', 'mess_author', 'mess_time', 'mess_cate', 'mess_price', 'mess_seenum','mess_hezuo', 'mess_ifsuccess',)
    search_fields = ('mess_title', 'mess_author', 'mess_time', 'mess_cate', 'mess_price', 'mess_seenum','mess_hezuo', 'mess_ifsuccess',)
    list_filter = ('mess_cate', 'mess_ifsuccess',)
    ordering = ('-mess_time',)

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

admin.site.register(Message, adminMess)