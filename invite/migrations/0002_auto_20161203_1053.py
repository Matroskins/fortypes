# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-03 10:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='from_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_invites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invite',
            name='user_who_used',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invited_by', to=settings.AUTH_USER_MODEL),
        ),
    ]