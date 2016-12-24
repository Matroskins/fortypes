from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from collections_posts.serializers import CollectionPostSerializer
from collections_posts.tests.factories import CollectionPostFactory, CollectionImagesBlockFactory, \
    CollectionImageFactory, CollectionTextFactory
from core.tests import AuthorizeForTestsMixin


class CollectionsTestCase(AuthorizeForTestsMixin, APITestCase):
    def setUp(self):
        super(CollectionsTestCase, self).setUp()
        self.collection_post = CollectionPostFactory(owner=self.user)
        self.collection_images_block = CollectionImagesBlockFactory(collection_post=self.collection_post)
        self.collection_image_1 = CollectionImageFactory(collection_post=self.collection_post)
        self.collection_image_2 = CollectionImageFactory(collection_post=self.collection_post,
                                                         block=self.collection_images_block)
        self.collection_image_3 = CollectionImageFactory(collection_post=self.collection_post,
                                                         block=self.collection_images_block)
        self.collection_text = CollectionTextFactory(collection_post=self.collection_post, order=1)
        self.collection_text_2 = CollectionTextFactory(collection_post=self.collection_post, order=2)
        self.url = reverse("collections-list")

    def test_get_all(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response.data[0]['images'][0]['image']['image_original'] = '/media/' + \
                                                                   response.data[0]['images'][0]['image'][
                                                                       'image_original'].split(
                                                                       '/')[-1]
        response.data[0]['images'][0]['image']['image_thumbnail'] = '/media/' + \
                                                                    response.data[0]['images'][0]['image'][
                                                                        'image_thumbnail'].split(
                                                                        '/')[-1]
        response.data[0]['images'][1]['image']['image_original'] = '/media/' + \
                                                                   response.data[0]['images'][1]['image'][
                                                                       'image_original'].split(
                                                                       '/')[-1]
        response.data[0]['images'][1]['image']['image_thumbnail'] = '/media/' + \
                                                                    response.data[0]['images'][1]['image'][
                                                                        'image_thumbnail'].split(
                                                                        '/')[-1]
        response.data[0]['images'][2]['image']['image_original'] = '/media/' + \
                                                                   response.data[0]['images'][2]['image'][
                                                                       'image_original'].split(
                                                                       '/')[-1]
        response.data[0]['images'][2]['image']['image_thumbnail'] = '/media/' + \
                                                                    response.data[0]['images'][2]['image'][
                                                                        'image_thumbnail'].split(
                                                                        '/')[-1]
        self.assertEqual(response.data, CollectionPostSerializer([self.collection_post], many=True).data)
