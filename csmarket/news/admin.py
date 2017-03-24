from django.contrib import admin
from news.models import cate,News,Words
# Register your models here.

class adminCate(admin.ModelAdmin):
    list_display = ('cate_name','cate_time','cate_num',)
    search_fields = ('cate_name','cate_time','cate_num',)
    list_filter = ('cate_name','cate_time','cate_num',)
    ordering = ('-cate_time',)

admin.site.register(cate, adminCate)

class adminNews(admin.ModelAdmin):
    list_display = ('new_title','new_author','new_time','new_seenum','new_cate',)
    search_fields =('new_title','new_author','new_time','new_seenum','new_cate','new_content',)
    list_filter =('new_author','new_seenum','new_cate',)
    ordering = ('-new_time',)

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
admin.site.register(News, adminNews)

class adminMessage(admin.ModelAdmin):
    list_display = ('new_id','father_id','m_time','m_people',)
    search_fields = ('new_id','father_id','m_content','m_time','m_people',)
    list_filter = ('father_id','m_people',)
    ordering = ('-m_time',)

admin.site.register(Words,adminMessage)