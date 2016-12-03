from django.contrib.auth.models import User
from django.db import models

from core.models import TimestampModel


class Invite(TimestampModel, models.Model):
    code = models.CharField(max_length=6, unique=True)
    used = models.BooleanField(default=False)
    from_user = models.ForeignKey(User, null=True, related_name='my_invites')
    user_who_used = models.ForeignKey(User, null=True, related_name='invited_by')
