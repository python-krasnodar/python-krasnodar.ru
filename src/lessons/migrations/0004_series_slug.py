# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_lesson_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='slug',
            field=models.SlugField(default='', max_length=128),
        ),
    ]