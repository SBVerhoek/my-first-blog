# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171221_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='h1',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
