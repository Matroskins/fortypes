from django.contrib.auth.models import User
from django.db import models

from fonts.models import Font


class UserFontRelation(models.Model):
    like = models.BooleanField(default=False)
    shared_facebook = models.BooleanField(default=False)
    shared_vk = models.BooleanField(default=False)
    shared_twitter = models.BooleanField(default=False)
    font = models.ForeignKey(Font, related_name='user_relation')
    user = models.ForeignKey(User, related_name='font_relation')
