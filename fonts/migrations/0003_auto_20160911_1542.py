# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 12:42
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fonts', '0002_symbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='font',
            name='image',
            field=models.ImageField(default=None, storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='font',
            name='status',
            field=models.SlugField(choices=[('private', 'private'), ('on_review', 'on_review'), ('public', 'public')], default='on_review'),
        ),
        migrations.AlterField(
            model_name='font',
            name='title',
            field=models.CharField(help_text='title', max_length=200),
        ),
    ]
