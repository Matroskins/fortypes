import factory

from accounts.tests.factories import UserFactory
from collections_posts.models import CollectionPost, CollectionImagesBlock, CollectionText, CollectionImage
from fonts.models import STATUS_PUBLIC
from fonts.tests.factories import ImageObjFactory


class CollectionPostFactory(factory.django.DjangoModelFactory):
    owner = factory.SubFactory(UserFactory)
    title = 'Scandinavian Design'
    up_title = 'early XX cen.'
    status = STATUS_PUBLIC

    class Meta:
        model = CollectionPost


class CollectionImagesBlockFactory(factory.django.DjangoModelFactory):
    collection_post = factory.SubFactory(CollectionPostFactory)
    order = 0

    class Meta:
        model = CollectionImagesBlock


class CollectionImageFactory(factory.django.DjangoModelFactory):
    image = factory.SubFactory(ImageObjFactory)
    collection_post = factory.SubFactory(CollectionPostFactory)
    order = 0

    # block = factory.SubFactory(CollectionImagesBlockFactory)
    class Meta:
        model = CollectionImage


class CollectionTextFactory(factory.django.DjangoModelFactory):
    text = 'Some text about Scandinavian Design'
    collection_post = factory.SubFactory(CollectionPostFactory)
    order = 0

    class Meta:
        model = CollectionText
