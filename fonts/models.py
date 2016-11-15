from django.contrib.auth.models import User
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.db.models.fields.related import OneToOneField

from accounts.models import Account
from core.models import ImageObj, ModelHasOwner

STATUS_PRIVATE = 'private'
STATUS_ON_REVIEW = 'on_review'
STATUS_PUBLIC = 'public'

STATUS_CHOICES = (
    (STATUS_PRIVATE, STATUS_PRIVATE),
    (STATUS_ON_REVIEW, STATUS_ON_REVIEW),
    (STATUS_PUBLIC, STATUS_PUBLIC)
)


class Font(ModelHasOwner, models.Model):
    content = models.CharField(max_length=200, help_text='content')
    author_name = models.CharField(max_length=500, help_text='author_name', blank=True, null=True)
    status = models.SlugField(choices=STATUS_CHOICES, default=STATUS_ON_REVIEW)
    image = OneToOneField(ImageObj)


class Symbol(models.Model):
    value = models.CharField(max_length=1)
    font = models.ForeignKey(Font, related_name='symbols')
    point_one_x = models.FloatField()
    point_one_y = models.FloatField()
    point_two_x = models.FloatField()
    point_two_y = models.FloatField()
