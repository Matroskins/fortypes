# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-03 10:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fonts', '0005_auto_20161203_1053'),
        ('invite', '0002_auto_20161203_1053'),
        ('accounts', '0002_auto_20161203_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
