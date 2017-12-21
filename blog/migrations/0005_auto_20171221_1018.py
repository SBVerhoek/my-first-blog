# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171221_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='docfile',
            field=models.FileField(blank=True, default=None, upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
