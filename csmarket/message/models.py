#-*-coding:utf-8 -*-
from django.db import models

# Create your models here.

class Cate(models.Model):
    cate_name = models.CharField(verbose_name="类别标题", max_length=30)
    cate_time = models.DateTimeField(verbose_name="添加时间")
    cate_num = models.IntegerField(verbose_name="类别编号", unique=True)

    def __str__(self):
        return self.cate_name

    class Meta:
        db_table = "cate_message_table"
        verbose_name = u'信息类别'
        verbose_name_plural = u'信息类别管理'

class Message(models.Model):
    mess_title = models.CharField(verbose_name='标题', max_length=30, blank=False)
    mess_image = models.ImageField(verbose_name='图像信息',height_field=100,width_field=100)
    mess_author = models.CharField(verbose_name='发布人', max_length=15, blank=False)
    mess_time = models.DateTimeField(verbose_name='发布时间')
    mess_cate = models.ForeignKey(Cate, verbose_name='类别', blank=False)
    mess_price = models.FloatField(verbose_name='交易报价',default=0.0)
    mess_seenum = models.IntegerField(verbose_name='浏览次数', default=0)
    mess_hezuo = models.CharField(verbose_name='合作方', max_length=15, blank=True)
    mess_ifsuccess = models.BooleanField(verbose_name='交易是否成功',default=False)
    mess_content = models.TextField(verbose_name='具体描述', blank=False)
    def __str__(self):
        return self.mess_title

    class Meta:
        db_table = "message_table"
        verbose_name = u'素材管理'
        verbose_name_plural = u'素材管理'

class Mwords(models.Model):
    mess_id = models.IntegerField(verbose_name='服务需求id',blank=False)
    father_id = models.IntegerField(verbose_name='父id',blank=True)
    mw_content=models.TextField(verbose_name='评论内容',blank=False)
    mw_time = models.DateTimeField(verbose_name='评论时间',blank=False)
    mw_people = models.CharField(verbose_name='留言人',max_length=15,blank=False)

    def __str__(self):
        return self.mess_id

    class Meta:
        db_table = 'message_words_table'
        verbose_name = u'服务需求留言'
        verbose_name_plural = '服务需求留言'