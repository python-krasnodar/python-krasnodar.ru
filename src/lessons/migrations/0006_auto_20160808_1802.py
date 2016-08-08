# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 18:02
from __future__ import unicode_literals

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_lesson_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=ckeditor.fields.RichTextField(default=None),
        ),
        migrations.AlterField(
            model_name='series',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
    ]