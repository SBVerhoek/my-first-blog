# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20171221_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='h1date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
