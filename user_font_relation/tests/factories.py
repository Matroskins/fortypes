import factory

from accounts.tests.factories import UserFactory
from fonts.tests.factories import FontFactory
from user_font_relation.models import UserFontRelation, AdminFontRelation


class UserFontRelationFactory(factory.django.DjangoModelFactory):
    font = factory.SubFactory(FontFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = UserFontRelation


class AdminFontRelationFactory(factory.django.DjangoModelFactory):
    font = factory.SubFactory(FontFactory)
    user = factory.SubFactory(UserFactory)
    moderated = True

    class Meta:
        model = AdminFontRelation
