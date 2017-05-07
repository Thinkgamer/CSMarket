# coding: utf8
from django.db import models

# Create your models here.

class example(models.Model):
    title = models.CharField(verbose_name='标题', max_length=30, blank=False)
    image = models.ImageField(blank=True,upload_to='example',verbose_name='案例封面')
    pub_date = models.DateTimeField(verbose_name='发布时间')
    see_num = models.IntegerField(verbose_name='浏览次数',default=0)
    service_obj = models.CharField(verbose_name="服务对象", max_length=30, blank=False)
    chengjiao_time = models.DateTimeField(verbose_name='成交时间')
    jianjie = models.TextField(verbose_name='简介',default="")
    show = models.TextField(verbose_name='内容',blank=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "example_table"
        verbose_name = u'案例'
        verbose_name_plural = u'案例素材'


class doc(models.Model):
    title = models.CharField(verbose_name='标题', max_length=30, blank=False)
    see_num = models.IntegerField(verbose_name='浏览次数',default=0)
    pub_date = models.DateTimeField(verbose_name='发布时间')
    show = models.TextField(verbose_name='内容', blank=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "doc_table"
        verbose_name = u'技术文档'
        verbose_name_plural = u'技术文档'
