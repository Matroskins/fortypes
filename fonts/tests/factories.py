import factory

from accounts.tests.factories import UserFactory
from core.models import ImageObj
from fonts.models import Font, Symbol
from user_font_relation.models import AdminFontRelation


class ImageObjFactory(factory.django.DjangoModelFactory):
    image_original = factory.django.ImageField(from_path='fonts/tests/test_file.jpg')
    image_thumbnail = factory.django.ImageField(from_path='fonts/tests/test_file.jpg')

    class Meta:
        model = ImageObj


class FontFactory(factory.django.DjangoModelFactory):
    owner = factory.SubFactory(UserFactory)
    content = 'THE'
    image = factory.SubFactory(ImageObjFactory)

    class Meta:
        model = Font


class SymbolFactory(factory.django.DjangoModelFactory):
    font = factory.SubFactory(FontFactory)
    value = 'T'
    point_one_x = 1.2
    point_one_y = 1.3
    point_two_x = 2.2
    point_two_y = 2.3

    class Meta:
        model = Symbol


class AdminFontRelationFactory(factory.django.DjangoModelFactory):
    font = factory.SubFactory(FontFactory)
    user = factory.SubFactory(UserFactory)
    moderated = True

    class Meta:
        model = AdminFontRelation
