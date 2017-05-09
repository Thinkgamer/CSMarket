#-*-coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # 手机号
    user_phone = models.CharField(blank=True, verbose_name='电话', max_length=11)

    # 学生身份认证信息
    user_eid=models.CharField(blank=True,max_length=19,verbose_name='身份证号')
    user_school=models.CharField(blank=True,max_length=20,verbose_name='学校名字')
    user_start_year=models.CharField(blank=True,max_length=4,verbose_name='入学年份')
    user_xueli=models.CharField(blank=True,max_length=10,verbose_name='学历')
    user_year=models.IntegerField(blank=True,verbose_name='几年制',default=4)
    user_xuehao=models.CharField(blank=True,max_length=20,verbose_name='学号')
    user_xszimg=models.ImageField(blank=True,upload_to='xszimg',verbose_name='学生证页面')

    # 信息补充
    user_qq = models.CharField(blank=True,verbose_name='QQ',max_length=10)
    user_wechat = models.CharField(blank=True,verbose_name='微信',max_length=15)
    user_shanchang = models.CharField(blank=True,verbose_name='擅长',max_length=50)
    user_xuanyan = models.CharField(blank=True,verbose_name='宣言',max_length=50)

    #判断是否是认证通过的用户
    user_isValid=models.BooleanField(blank=True,default=False)

    def __unicode__(self):
        return self.user.username
