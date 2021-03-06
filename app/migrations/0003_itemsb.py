# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170624_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemsb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50, verbose_name='项目名称')),
                ('applyyear', models.DateTimeField(max_length=20, verbose_name='申报年份')),
                ('itemtypes', models.CharField(max_length=30, verbose_name='经费来源')),
                ('types2', models.CharField(max_length=30, verbose_name='经费项目')),
                ('types3', models.CharField(max_length=30, verbose_name='具体项目')),
                ('f_xiao', models.CharField(max_length=20, verbose_name='经费额度')),
                ('fuzeren', models.CharField(max_length=20, verbose_name='负责人')),
                ('zhiwu', models.CharField(max_length=20, verbose_name='职务')),
                ('tel2', models.CharField(max_length=12, verbose_name='负责人电话')),
                ('email1', models.CharField(max_length=20, verbose_name='负责人邮箱')),
                ('lxren', models.CharField(max_length=20, verbose_name='联系人')),
                ('tel', models.CharField(max_length=20, verbose_name='联系人电话')),
            ],
        ),
    ]
