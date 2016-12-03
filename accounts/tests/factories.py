import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = 'test_username'
    first_name = 'Alex'
    last_name = 'Tester'

    class Meta:
        model = User
