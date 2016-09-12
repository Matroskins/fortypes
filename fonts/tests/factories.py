import factory

from accounts.tests.factories import AccountFactory
from fonts.models import Font


class FontFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(AccountFactory)

    class Meta:
        model = Font

