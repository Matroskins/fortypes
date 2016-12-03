from django.contrib.auth.models import User
from django.db import models

from core.models import TimestampModel


class ModelHasOwner(models.Model):
    owner = models.ForeignKey(User)

    class Meta:
        abstract = True
