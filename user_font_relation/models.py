from django.contrib.auth.models import User
from django.db import models

from core.models import TimestampModel
from fonts.models import Font, STATUS_PUBLIC


class UserFontRelation(models.Model):
    like = models.BooleanField(default=False)
    shared_facebook = models.BooleanField(default=False)
    shared_vk = models.BooleanField(default=False)
    shared_twitter = models.BooleanField(default=False)
    font = models.ForeignKey(Font, related_name='user_relation')
    user = models.ForeignKey(User, related_name='font_relation')


class AdminFontRelation(TimestampModel, models.Model):
    moderated = models.BooleanField(default=False)
    font = models.ForeignKey(Font, related_name='admin_relation')
    user = models.ForeignKey(User, related_name='admin_font_relation')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.moderated is True and (self.user.is_superuser or self.user.is_staff):
            self.font.status = STATUS_PUBLIC
            self.font.save()
