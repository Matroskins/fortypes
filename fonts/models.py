from django.contrib.auth.models import User
from django.db import models
from django.db.models import ImageField
from django.core.files.storage import FileSystemStorage

from accounts.models import Account


storage = FileSystemStorage(location='media/')

STATUS_PRIVATE = 'private'
STATUS_ON_REVIEW = 'on_review'
STATUS_PUBLIC = 'public'

STATUS_CHOICES = (
    (STATUS_PRIVATE, STATUS_PRIVATE),
    (STATUS_ON_REVIEW, STATUS_ON_REVIEW),
    (STATUS_PUBLIC, STATUS_PUBLIC)
)


class Font(models.Model):
    title = models.CharField(max_length=200, help_text='test text')
    author = models.ForeignKey(Account, related_name='fonts')
    status = models.SlugField(choices=STATUS_CHOICES)
    # image = ImageField(storage=storage)
    # photo_small = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
    #                               ResizeToFill(50, 50)], image_field='photo',
    #                              format='JPEG', options={'quality': 90})


class Symbol(models.Model):
    position = models.IntegerField()
    font = models.ForeignKey(Font, related_name='symbols')
    ul_point = models.PositiveSmallIntegerField()
    ur_point = models.PositiveSmallIntegerField()
    dl_point = models.PositiveSmallIntegerField()
    dr_point = models.PositiveSmallIntegerField()
