from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import ImageField
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from fortypes.settings.base import MEDIA_ROOT

storage = FileSystemStorage(location=MEDIA_ROOT)


class ImageObj(models.Model):
    image_original = ImageField(storage=storage, )
    image_thumbnail = ProcessedImageField([
        ResizeToFill(100, 100)], storage=storage,
        format='JPEG', options={'quality': 90}, null=True)


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
