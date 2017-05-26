#-×-coding:utf-8-*-
from django.contrib import admin
from message.models import Cate,Message,Mwords,DCate,DMessage,DMwords

# Register your models here.
class adminCate(admin.ModelAdmin):
    list_display = ('cate_name','cate_time','cate_num',)
    search_fields = ('cate_name','cate_time','cate_num',)
    list_filter = ('cate_name','cate_time','cate_num',)
    ordering = ('-cate_time',)

admin.site.register(Cate, adminCate)

class adminMess(admin.ModelAdmin):
    # mess_title  mess_author  mess_time  mess_cate  mess_price  mess_seenum  mess_hezuo mess_ifsuccess
    list_display = ('mess_title', 'mess_author', 'mess_time', 'mess_cate', 'mess_price', 'mess_xuorfu', 'mess_seenum','mess_totalnum','mess_compeletenum','mess_hezuo', 'mess_ifsuccess',)
    search_fields = ('mess_title', 'mess_author', 'mess_time', 'mess_cate', 'mess_price', 'mess_xuorfu', 'mess_seenum','mess_totalnum','mess_compeletenum','mess_hezuo', 'mess_ifsuccess',)
    list_filter = ('mess_cate', 'mess_ifsuccess', 'mess_xuorfu',)
    ordering = ('-mess_time',)

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
admin.site.register(Message, adminMess)

class adminMwords(admin.ModelAdmin):
    # mess_id   father_id  mw_content  mw_time mw_people
    list_display = ('mess_id','father_id','mw_time','mw_people',)
    search_fields = ('mess_id','father_id','mw_content','mw_time','mw_people',)
    list_filter = ('father_id','mw_people',)
    ordering = ('-mw_time',)

admin.site.register(Mwords,adminMwords)

# --- 代办 ---
class adminCate(admin.ModelAdmin):
    list_display = ('dcate_name','dcate_time','dcate_num',)
    search_fields = ('dcate_name','dcate_time','dcate_num',)
    list_filter = ('dcate_name','dcate_time','dcate_num',)
    ordering = ('-dcate_time',)

admin.site.register(DCate, adminCate)

class adminMess(admin.ModelAdmin):
    # mess_title  mess_author  mess_time  mess_cate  mess_price  mess_seenum  mess_hezuo mess_ifsuccess
    list_display = ('dmess_title', 'dmess_author', 'dmess_time', 'dmess_cate', 'dmess_price', 'dmess_seenum','dmess_totalnum','dmess_compeletenum','dmess_hezuo', 'dmess_ifsuccess',)
    search_fields = ('dmess_title', 'dmess_author', 'dmess_time', 'dmess_cate', 'dmess_price', 'dmess_seenum','dmess_totalnum','dmess_compeletenum','dmess_hezuo', 'dmess_ifsuccess',)
    list_filter = ('dmess_cate', 'dmess_ifsuccess',)
    ordering = ('-dmess_time',)

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
admin.site.register(DMessage, adminMess)

class adminMwords(admin.ModelAdmin):
    # mess_id   father_id  mw_content  mw_time mw_people
    list_display = ('dmess_id','dfather_id','dmw_time','dmw_people',)
    search_fields = ('dmess_id','dfather_id','dmw_content','dmw_time','dmw_people',)
    list_filter = ('dfather_id','dmw_people',)
    ordering = ('-dmw_time',)

admin.site.register(DMwords,adminMwords)