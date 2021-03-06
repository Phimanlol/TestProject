# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-06 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181006_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='category',
            field=models.CharField(choices=[('adopting', '宠物领养'), ('having', '宠物送养')], max_length=10, verbose_name='是否领养'),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('male', '先生'), ('female', '女士')], max_length=2, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号'),
        ),
    ]
