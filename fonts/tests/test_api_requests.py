import codecs
import os

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.tests.factories import AccountFactory
from core.tests import AuthorizeForTestsMixin
from fonts.models import Font
from fonts.serializers import FontSerializer
from fortypes.settings.base import BASE_DIR


class FontCreateTestCase(AuthorizeForTestsMixin, APITestCase):

    def setUp(self):
        super(FontCreateTestCase, self).setUp()
        self.account = AccountFactory(user=self.user)
        self.url = reverse('fonts-list')

    def test_create_font(self):
        self.data = {
            'title': 'title',
            'author': self.account,
            # 'image': None,
            'symbols': [
                {'position': 1,
                 'ul_point': 0.2,
                 'ur_point': 0.3,
                 'dl_point': 0.4,
                 'dr_point': 0.5,
                 },
                {'position': 2,
                 'ul_point': 0.6,
                 'ur_point': 0.7,
                 'dl_point': 0.8,
                 'dr_point': 0.9,
                 }
            ],
        }
        with codecs.open(os.path.join(os.path.dirname(BASE_DIR), 'fonts', 'tests', 'test_file.jpg'), 'r') as test_file:
            self.data.update({'file ': test_file, 'filename': 'test_file.jpg'})
            response = self.client.post(self.url, self.data, content_type='application/json')
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Font.objects.get(author=self.account))
        # self.expected['id'] = int(response.data['id'])
        # self.assertEqual(response.data, self.expected)