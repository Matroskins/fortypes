import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.tests.factories import AccountFactory
from core.tests import AuthorizeForTestsMixin
from fonts.models import Font, Symbol
from fonts.serializers import FontSerializer, SymbolForFontSerializer
from fonts.tests.factories import ImageObjFactory, FontFactory, SymbolFactory


class FontCreateTestCase(AuthorizeForTestsMixin, APITestCase):
    def setUp(self):
        super(FontCreateTestCase, self).setUp()
        self.account = AccountFactory(user=self.user)
        self.url = reverse("fonts-list")
        self.image_id = ImageObjFactory().pk

    def test_create_font_with_image(self):
        self.data = {
            "title": "title",
            "content": "ab",
            "image_id": self.image_id,
            "symbols": [
                {"value": "a",
                 "point_one_x": 0.2,
                 "point_one_y": 0.3,
                 "point_two_x": 0.4,
                 "point_two_y": 0.5,
                 },
                {"value": "b",
                 "point_one_x": 0.6,
                 "point_one_y": 0.7,
                 "point_two_x": 0.8,
                 "point_two_y": 0.9,
                 },
            ],
        }
        response = self.client.post(self.url, data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        font = Font.objects.get(owner=self.account)
        response.data['image']['image_original'] = '/media/' + response.data['image']['image_original'].split('/')[-1]
        response.data['image']['image_thumbnail'] = '/media/' + response.data['image']['image_thumbnail'].split('/')[-1]
        self.assertEqual(response.data, FontSerializer(font).data)

        symbol_1_data = SymbolForFontSerializer(Symbol.objects.all()[0]).data
        symbol_2_data = SymbolForFontSerializer(Symbol.objects.all()[1]).data
        self.assertIn(symbol_1_data, response.data['symbols'])
        self.assertIn(symbol_2_data, response.data['symbols'])


class FontsGetTestCase(AuthorizeForTestsMixin, APITestCase):
    def setUp(self):
        super(FontsGetTestCase, self).setUp()
        self.account = AccountFactory(user=self.user)
        self.font_1 = FontFactory(owner=self.account)
        self.font_2 = FontFactory(owner=self.account, author_name='Mr. Writer')
        self.symbol_1 = SymbolFactory(font=self.font_1)
        self.symbol_2 = SymbolFactory(font=self.font_1)
        self.symbol_3 = SymbolFactory(font=self.font_2)
        self.url = reverse("fonts-list")

    def test_get_font_with_image(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data[0]['image']['image_original'] = '/media/' + \
                                                      response.data[0]['image']['image_original'].split('/')[-1]
        response.data[1]['image']['image_original'] = '/media/' + \
                                                      response.data[1]['image']['image_original'].split('/')[-1]
        response.data[0]['image']['image_thumbnail'] = '/media/' + \
                                                       response.data[0]['image']['image_thumbnail'].split('/')[-1]
        response.data[1]['image']['image_thumbnail'] = '/media/' + \
                                                       response.data[1]['image']['image_thumbnail'].split('/')[-1]

        self.assertEqual(response.data, [FontSerializer(self.font_1).data, FontSerializer(self.font_2).data])
        self.assertEqual(response.data[0]['author_name'],
                         " ".join((self.account.user.first_name, self.account.user.last_name)))
        self.assertEqual(response.data[1]['author_name'], 'Mr. Writer')

        symbol_1_data = SymbolForFontSerializer(self.symbol_1).data
        symbol_2_data = SymbolForFontSerializer(self.symbol_2).data
        symbol_3_data = SymbolForFontSerializer(self.symbol_3).data
        self.assertIn(symbol_1_data, response.data[0]['symbols'])
        self.assertIn(symbol_2_data, response.data[0]['symbols'])
        self.assertIn(symbol_3_data, response.data[1]['symbols'])
