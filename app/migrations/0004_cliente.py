# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_itemsb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('filhos', models.IntegerField()),
                ('ativo', models.NullBooleanField()),
            ],
        ),
    ]
