# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-24 12:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_imageobj_image_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionImagesBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('up_title', models.CharField(max_length=500)),
                ('status', models.SlugField(choices=[('private', 'private'), ('on_review', 'on_review'), ('public', 'public')], default='on_review')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CollectionText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('collection_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='collections_posts.CollectionPost')),
            ],
        ),
        migrations.AddField(
            model_name='collectionimagesblock',
            name='collection_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_blocks', to='collections_posts.CollectionPost'),
        ),
        migrations.AddField(
            model_name='collectionimage',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='collections_posts.CollectionImagesBlock'),
        ),
        migrations.AddField(
            model_name='collectionimage',
            name='collection_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='collections_posts.CollectionPost'),
        ),
        migrations.AddField(
            model_name='collectionimage',
            name='image',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ImageObj'),
        ),
    ]
