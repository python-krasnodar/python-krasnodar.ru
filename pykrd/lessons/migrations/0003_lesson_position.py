# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_lesson_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
