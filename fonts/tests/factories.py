import factory

from accounts.tests.factories import AccountFactory
from core.models import ImageObj
from fonts.models import Font


class FontFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(AccountFactory)

    class Meta:
        model = Font


class ImageObjFactory(factory.django.DjangoModelFactory):
    image_original = factory.django.FileField(filename='test_file.jpg')

    class Meta:
        model = ImageObj
