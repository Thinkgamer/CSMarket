# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-25 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20170407_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='DCate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcate_name', models.CharField(max_length=30, verbose_name='类别标题')),
                ('dcate_time', models.DateTimeField(verbose_name='添加时间')),
                ('dcate_num', models.IntegerField(unique=True, verbose_name='类别编号')),
            ],
            options={
                'verbose_name': '代办类别',
                'db_table': 'dcate_message_table',
                'verbose_name_plural': '代办类别管理',
            },
        ),
        migrations.CreateModel(
            name='DMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dmess_title', models.CharField(max_length=30, unique=True, verbose_name='标题')),
                ('dmess_image', models.CharField(blank=True, max_length=100, verbose_name='图像信息')),
                ('dmess_author', models.CharField(max_length=15, verbose_name='发布人')),
                ('dmess_time', models.DateTimeField(verbose_name='发布时间')),
                ('dmess_price', models.FloatField(default=0.0, verbose_name='交易报价')),
                ('dmess_seenum', models.IntegerField(default=0, verbose_name='浏览次数')),
                ('dmess_hezuo', models.CharField(blank=True, max_length=15, verbose_name='合作方')),
                ('dmess_ifsuccess', models.BooleanField(default=False, verbose_name='交易是否成功')),
                ('dmess_content', models.TextField(verbose_name='具体描述')),
            ],
            options={
                'verbose_name': '代办素材管理',
                'db_table': 'dmessage_table',
                'verbose_name_plural': '代办素材管理',
            },
        ),
        migrations.CreateModel(
            name='DMwords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dmess_id', models.IntegerField(verbose_name='代办id')),
                ('dfather_id', models.IntegerField(blank=True, verbose_name='父id')),
                ('dmw_content', models.TextField(verbose_name='评论内容')),
                ('dmw_time', models.DateTimeField(verbose_name='评论时间')),
                ('dmw_people', models.CharField(max_length=15, verbose_name='留言人')),
            ],
            options={
                'verbose_name': '代办留言管理',
                'db_table': 'dmessage_words_table',
                'verbose_name_plural': '代办留言管理',
            },
        ),
        migrations.AlterModelOptions(
            name='cate',
            options={'verbose_name': '信息类别', 'verbose_name_plural': '需求/服务类别管理'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': '需求/服务素材管理', 'verbose_name_plural': '需求/服务素材管理'},
        ),
        migrations.AlterModelOptions(
            name='mwords',
            options={'verbose_name': '需求/服务留言管理', 'verbose_name_plural': '需求/服务留言管理'},
        ),
        migrations.AlterField(
            model_name='message',
            name='mess_title',
            field=models.CharField(max_length=30, unique=True, verbose_name='标题'),
        ),
        migrations.AddField(
            model_name='dmessage',
            name='dmess_cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.Cate', verbose_name='类别'),
        ),
    ]