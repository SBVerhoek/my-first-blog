# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171221_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='h1date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='h1image',
            field=models.FileField(blank=True, default=None, null=True, upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='h1text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
