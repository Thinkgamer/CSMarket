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
        verbose_name_plural = u'需求/服务类别管理'

class Message(models.Model):
    mess_title = models.CharField(verbose_name='标题', max_length=30, blank=False, unique=True)
    mess_image = models.ImageField(verbose_name='图像信息',blank=True,upload_to='fengmian')
    mess_author = models.CharField(verbose_name='发布人', max_length=15, blank=False)
    mess_time = models.DateTimeField(verbose_name='发布时间')
    mess_cate = models.ForeignKey(Cate, verbose_name='类别', blank=False)
    mess_price = models.FloatField(verbose_name='交易报价',default=0.0)
    mess_xuorfu = models.CharField(verbose_name='需求or服务',max_length=2,default=None)
    mess_seenum = models.IntegerField(verbose_name='浏览次数', default=0)
    mess_hezuo = models.CharField(verbose_name='合作方', max_length=15, blank=True)
    mess_ifsuccess = models.BooleanField(verbose_name='交易是否成功',default=False)
    mess_content = models.TextField(verbose_name='具体描述', blank=False)
    def __str__(self):
        return self.mess_title

    class Meta:
        db_table = "message_table"
        verbose_name = u'需求/服务素材管理'
        verbose_name_plural = u'需求/服务素材管理'

class Mwords(models.Model):
    mess_id = models.IntegerField(verbose_name='服务需求id',blank=False)
    father_id = models.IntegerField(verbose_name='父id',blank=True)
    mw_content=models.TextField(verbose_name='评论内容',blank=False)
    mw_time = models.DateTimeField(verbose_name='评论时间',blank=False)
    mw_people = models.CharField(verbose_name='留言人',max_length=15,blank=False)

    def __str__(self):
        return str(self.mess_id)

    class Meta:
        db_table = 'message_words_table'
        verbose_name = u'需求/服务留言管理'
        verbose_name_plural = '需求/服务留言管理'

# ------------------------代办中心-----------------

class DCate(models.Model):
    dcate_name = models.CharField(verbose_name="类别标题", max_length=30)
    dcate_time = models.DateTimeField(verbose_name="添加时间")
    dcate_num = models.IntegerField(verbose_name="类别编号", unique=True)

    def __str__(self):
        return self.dcate_name

    class Meta:
        db_table = "dcate_message_table"
        verbose_name = u'代办类别'
        verbose_name_plural = u'代办类别管理'

class DMessage(models.Model):
    dmess_title = models.CharField(verbose_name='标题', max_length=30, blank=False, unique=True)
    dmess_image = models.ImageField(verbose_name='图像信息',blank=True,upload_to='fengmian')
    dmess_author = models.CharField(verbose_name='发布人', max_length=15, blank=False)
    dmess_time = models.DateTimeField(verbose_name='发布时间')
    dmess_cate = models.ForeignKey(DCate, verbose_name='类别', blank=False)
    dmess_price = models.FloatField(verbose_name='交易报价',default=0.0)
    dmess_seenum = models.IntegerField(verbose_name='浏览次数', default=0)
    dmess_hezuo = models.CharField(verbose_name='合作方', max_length=15, blank=True)
    dmess_ifsuccess = models.BooleanField(verbose_name='交易是否成功',default=False)
    dmess_content = models.TextField(verbose_name='具体描述', blank=False)
    def __str__(self):
        return self.dmess_title

    class Meta:
        db_table = "dmessage_table"
        verbose_name = u'代办素材管理'
        verbose_name_plural = u'代办素材管理'

class DMwords(models.Model):
    dmess_id = models.IntegerField(verbose_name='代办id',blank=False)
    dfather_id = models.IntegerField(verbose_name='父id',blank=True)
    dmw_content=models.TextField(verbose_name='评论内容',blank=False)
    dmw_time = models.DateTimeField(verbose_name='评论时间',blank=False)
    dmw_people = models.CharField(verbose_name='留言人',max_length=15,blank=False)

    def __str__(self):
        return str(self.dmess_id)

    class Meta:
        db_table = 'dmessage_words_table'
        verbose_name = u'代办留言管理'
        verbose_name_plural = '代办留言管理'