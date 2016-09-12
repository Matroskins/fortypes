import factory
from django.contrib.auth.models import User

from accounts.models import Account


class UserFactory(factory.django.DjangoModelFactory):
    username = 'test_username'

    class Meta:
        model = User


class AccountFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Account
