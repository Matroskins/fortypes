from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class UserModelEmailBackend(ModelBackend):
    def authenticate(self, email="", password="", **kwargs):
        try:
            user = User.objects.get(email__iexact=email)
            if check_password(password, user.password):
                return user
            else:
                return None
        except User.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None
