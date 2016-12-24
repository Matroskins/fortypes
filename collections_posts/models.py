from django.db import models
from django.db.models import OneToOneField

from accounts.models import ModelHasOwner
from core.models import TimestampModel, ImageObj
from fonts.models import STATUS_CHOICES, STATUS_ON_REVIEW


class CollectionPost(ModelHasOwner, TimestampModel):
    title = models.CharField(max_length=200)
    up_title = models.CharField(max_length=500)
    status = models.SlugField(choices=STATUS_CHOICES, default=STATUS_ON_REVIEW)


class CollectionImagesBlock(models.Model):
    collection_post = models.ForeignKey(CollectionPost, related_name='images_blocks')
    order = models.PositiveSmallIntegerField(default=0)


class CollectionImage(models.Model):
    image = OneToOneField(ImageObj)
    collection_post = models.ForeignKey(CollectionPost, related_name='images')
    order = models.PositiveSmallIntegerField(default=0)
    block = models.ForeignKey(CollectionImagesBlock, related_name='images', null=True)


class CollectionText(models.Model):
    text = models.TextField()
    collection_post = models.ForeignKey(CollectionPost, related_name='texts')
    order = models.PositiveSmallIntegerField(default=0)
