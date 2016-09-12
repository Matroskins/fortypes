from django.contrib.auth.models import User
from django.db import models
from django.db.models import ImageField
from django.core.files.storage import FileSystemStorage
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

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
    title = models.CharField(max_length=200, help_text='title')
    author = models.ForeignKey(Account, related_name='fonts')
    status = models.SlugField(choices=STATUS_CHOICES, default=STATUS_ON_REVIEW)
    image = ImageField(storage=storage)
    image_thumbnail = ImageSpecField([  #[Adjust(contrast=1.2, sharpness=1.1),
                                  ResizeToFill(100, 100)], source='image',
                                 format='JPEG', options={'quality': 90})


class Symbol(models.Model):
    position = models.IntegerField(unique=True)
    font = models.ForeignKey(Font, related_name='symbols')
    ul_point = models.FloatField()
    ur_point = models.FloatField()
    dl_point = models.FloatField()
    dr_point = models.FloatField()
