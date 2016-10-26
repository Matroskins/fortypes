import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.tests.factories import AccountFactory
from core.tests import AuthorizeForTestsMixin
from fonts.models import Font, Symbol
from fonts.serializers import FontSerializer, SymbolForFontSerializer


class FontCreateTestCase(AuthorizeForTestsMixin, APITestCase):
    def setUp(self):
        super(FontCreateTestCase, self).setUp()
        self.account = AccountFactory(user=self.user)
        self.url = reverse("fonts-list")

    def test_create_font_no_image(self):
        self.data = {
            "title": "title",
            "author": self.account.id,
            "content": "ab",
            # "image": None,
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
        # with open(os.path.join(os.path.dirname(BASE_DIR), "fonts", "tests", "test_file.jpg"), "r") as test_file:
        #     self.data.update({"file": test_file, "filename": "test_file.jpg"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        font = Font.objects.get(author=self.account)
        self.assertEqual(response.data, FontSerializer(font).data)

        symbol_1_data = SymbolForFontSerializer(Symbol.objects.all()[0]).data
        symbol_2_data = SymbolForFontSerializer(Symbol.objects.all()[1]).data
        self.assertIn(symbol_1_data, response.data['symbols'])
        self.assertIn(symbol_2_data, response.data['symbols'])
        # self.assertEqual(response.data, self.expected)
