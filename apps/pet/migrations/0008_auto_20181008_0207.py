# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 02:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0007_auto_20181006_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='宠物主人'),
        ),
    ]
