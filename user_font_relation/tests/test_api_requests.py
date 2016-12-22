from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.tests.factories import UserFactory
from core.tests import AuthorizeForTestsMixin
from fonts.tests.factories import FontFactory
from user_font_relation.models import UserFontRelation
from user_font_relation.serializers import UserFontRelationSerializer
from user_font_relation.tests.factories import UserFontRelationFactory


class FontsGetTestCase(AuthorizeForTestsMixin, APITestCase):
    def setUp(self):
        super(FontsGetTestCase, self).setUp()
        self.font_1 = FontFactory(owner=self.user)
        self.font_2 = FontFactory(owner=self.user)
        self.user_font_relation_1 = UserFontRelationFactory(user=self.user, font=self.font_1)
        self.url_list = reverse('fonts-relations-list')
        self.url_1 = reverse('fonts-relations-detail', args=(self.font_1.pk,))
        self.url_2 = reverse('fonts-relations-detail', args=(self.font_2.pk,))

    def test_get_font_relation(self):
        response = self.client.get(self.url_1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, UserFontRelationSerializer(self.user_font_relation_1).data)

    def test_get_font_relations_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [UserFontRelationSerializer(self.user_font_relation_1).data])

    def test_not_my_relation(self):
        self.client.force_authenticate(user=UserFactory(username='user_2'))
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_not_exist(self):
        response = self.client.get(reverse('fonts-relations-detail', args=(5,)))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'detail': 'Not found.'})

    def test_create_before_update_patch(self):
        self.assertFalse(UserFontRelation.objects.filter(user=self.user, font=self.font_2).all().exists())
        response = self.client.patch(self.url_2, data={'like': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        relation = UserFontRelation.objects.get(user=self.user, font=self.font_2)
        self.assertEqual(relation.like, True)

    def test_patch_exists(self):
        UserFontRelationFactory(user=self.user, font=self.font_2, like=True)
        response = self.client.patch(self.url_2, data={'like': False})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        relation = UserFontRelation.objects.get(user=self.user, font=self.font_2)
        self.assertEqual(relation.like, False)
