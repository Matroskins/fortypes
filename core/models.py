from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import ImageField
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from accounts.models import Account
from fortypes.settings.base import MEDIA_ROOT

storage = FileSystemStorage(location=MEDIA_ROOT)


class ModelHasOwner(models.Model):
    owner = models.ForeignKey(Account)

    class Meta:
        abstract = True


class ImageObj(models.Model):
    image_original = ImageField(storage=storage, )
    image_thumbnail = ProcessedImageField([
        ResizeToFill(100, 100)], storage=storage,
        format='JPEG', options={'quality': 90})
