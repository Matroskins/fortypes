from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import ImageField
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from accounts.models import Account

storage = FileSystemStorage(location='media/')


class ModelHasAuthor(models.Model):
    author = models.ForeignKey(Account)

    class Meta:
        abstract = True


class ImageObj(models.Model):
    image_original = ImageField(storage=storage)
    image_thumbnail = ImageSpecField([  # [Adjust(contrast=1.2, sharpness=1.1),
        ResizeToFill(100, 100)], source='image_original',
        format='JPEG', options={'quality': 90})
