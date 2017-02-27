#-*-coding: utf-8 -*-
from django.db import models

# Create your models here.

# #用户模型
# class User(models.Model):
#     #用户名,邮箱,密码
#     user_name = models.CharField(blank=False,max_length=15,verbose_name='用户名')
#     user_eamil = models.EmailField(blank=False,verbose_name='邮箱')
#     user_passwd = models.CharField(blank=False,max_length=50,verbose_name='密码')
#
#     #手机号
#     user_phone = models.CharField(blank=True,verbose_name='电话',max_length=11)
#
#     #学生身份认证信息
#     user_id=models.CharField(blank=True,max_length=19,verbose_name='身份证号')
#     user_school=models.CharField(blank=True,max_length=20,verbose_name='学校名字')
#     user_start_year=models.CharField(blank=True,max_length=4,verbose_name='入学年份')
#     user_xueli=models.CharField(blank=True,max_length=2,verbose_name='学历')
#     user_year=models.IntegerField(blank=True,verbose_name='几年制')
#     user_xuehao=models.CharField(blank=True,verbose_name='学号')
#     user_xszimg1=models.ImageField(blank=True,upload_to='xszimg1')
#     user_xszimg2 = models.ImageField(blank=True,upload_to='xszimg2')
#
#     #信息补充
#     user_qq = models.CharField(blank=True,verbose_name='QQ',max_length=10)
#     user_wechat = models.CharField(blank=True,verbose_name='微信',max_length=15)
#     user_shanchang = models.CharField(blank=True,verbose_name='擅长',max_length=50)
#     user_xuanyan = models.CharField(blank=True,verbose_name='宣言',max_length=50)
#
#     #注册信息和最后一次修改信息时间
#     user_registerTime=models.DateTimeField(verbose_name='注册时间')
#     user_lastLoginTime=models.DateTimeField(verbose_name='最后一次登录时间')
#
#     def __unicode__(self):
#         return self.user_name
#     class Meta:
#         db_table="user"