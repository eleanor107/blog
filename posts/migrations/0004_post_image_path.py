# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-01 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160330_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_path',
            field=models.TextField(default=''),
        ),
    ]
