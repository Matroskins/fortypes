import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.tests.factories import UserFactory
from core.models import ImageObj
from core.serializers import ImageObjOutSerializer
from core.tests import AuthorizeForTestsMixin
from fonts.models import Font, Symbol, STATUS_ON_REVIEW, Author
from fonts.serializers import SymbolForFontSerializer, FontCountSerializer, FontGetSerializer
from fonts.tests.factories import ImageObjFactory, FontFactory, SymbolFactory, AuthorFactory
from user_font_relation.tests.factories import AdminFontRelationFactory


class FontCreateTestCase(AuthorizeForTestsMixin, APITestCase):
    def setUp(self):
        super(FontCreateTestCase, self).setUp()
        self.url = reverse("fonts-list")
        self.image_id = ImageObjFactory().pk
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

    def test_create_font_with_image_no_author_name(self):
        response = self.client.post(self.url, data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        font = Font.objects.get(owner=self.user)
        response.data['image']['image_original'] = '/media/' + response.data['image']['image_original'].split('/')[-1]
        response.data['image']['image_thumbnail'] = '/media/' + response.data['image']['image_thumbnail'].split('/')[-1]
        serialized_font = FontGetSerializer(font).data
        self.assertEqual(response.data, serialized_font)
        self.assertEqual(serialized_font['author_name'], 'Alex Tester')
        self.assertEqual(Author.objects.all().count(), 0)

        symbol_1_data = SymbolForFontSerializer(Symbol.objects.all()[0]).data
        symbol_2_data = SymbolForFontSerializer(Symbol.objects.all()[1]).data
        self.assertIn(symbol_1_data, response.data['symbols'])
        self.assertIn(symbol_2_data, response.data['symbols'])

    def test_create_font_with_image_new_author_name(self):
        self.data['author_name'] = 'Some Author'
        self.assertEqual(Author.objects.all().count(), 0)
        response = self.client.post(self.url, data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        font = Font.objects.get(owner=self.user)
        response.data['image']['image_original'] = '/media/' + response.data['image']['image_original'].split('/')[-1]
        response.data['image']['image_thumbnail'] = '/media/' + response.data['image']['image_thumbnail'].split('/')[-1]
        serialized_font = FontGetSerializer(font).data
        self.assertEqual(response.data, serialized_font)
        self.assertEqual(font.author.name, 'Some Author')
        author = Author.objects.get()
        self.assertEqual(font.author, author)

        symbol_1_data = SymbolForFontSerializer(Symbol.objects.all()[0]).data
        symbol_2_data = SymbolForFontSerializer(Symbol.objects.all()[1]).data
        self.assertIn(symbol_1_data, response.data['symbols'])
        self.assertIn(symbol_2_data, response.data['symbols'])

    def test_create_font_with_image_exist_author(self):
        self.author = AuthorFactory(name='Some Author')
        self.assertEqual(Author.objects.all().count(), 1)
        self.data['author_name'] = 'Some Author'
        response = self.client.post(self.url, data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        font = Font.objects.get(owner=self.user)
        response.data['image']['image_original'] = '/media/' + response.data['image']['image_original'].split('/')[-1]
        response.data['image']['image_thumbnail'] = '/media/' + response.data['image']['image_thumbnail'].split('/')[-1]
        serialized_font = FontGetSerializer(font).data
        self.assertEqual(response.data, serialized_font)

        self.assertEqual(Author.objects.all().count(), 1)
        self.assertEqual(font.author.name, 'Some Author')
        self.assertEqual(font.author, self.author)

        symbol_1_data = SymbolForFontSerializer(Symbol.objects.all()[0]).data
        symbol_2_data = SymbolForFontSerializer(Symbol.objects.all()[1]).data
        self.assertIn(symbol_1_data, response.data['symbols'])
        self.assertIn(symbol_2_data, response.data['symbols'])


class FontsGetTestCase(APITestCase):
    def setUp(self):
        super(FontsGetTestCase, self).setUp()
        self.user = UserFactory(is_superuser=True, username='user_admin_1')
        self.client.force_authenticate(user=self.user)
        self.author = AuthorFactory(name='Mr. Writer')
        self.font_1 = FontFactory(owner=self.user, content='THE')
        self.font_2 = FontFactory(owner=self.user, author=self.author, content='HER')
        self.admin_font_relation = AdminFontRelationFactory(user=self.user, font=self.font_1)
        self.admin_font_relation_2 = AdminFontRelationFactory(user=self.user, font=self.font_2)
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

        self.assertEqual(response.data, [FontGetSerializer(self.font_1).data, FontGetSerializer(self.font_2).data])
        self.assertEqual(response.data[0]['author_name'],
                         " ".join((self.user.first_name, self.user.last_name)))
        self.assertEqual(response.data[1]['author_name'], 'Mr. Writer')

        symbol_1_data = SymbolForFontSerializer(self.symbol_1).data
        symbol_2_data = SymbolForFontSerializer(self.symbol_2).data
        symbol_3_data = SymbolForFontSerializer(self.symbol_3).data
        self.assertIn(symbol_1_data, response.data[0]['symbols'])
        self.assertIn(symbol_2_data, response.data[0]['symbols'])
        self.assertIn(symbol_3_data, response.data[1]['symbols'])

    def test_get_font_search_no_filter(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_font_search_no_filter_one_no_moderated(self):
        self.user_not_admin = UserFactory(is_superuser=False, username='user_no_admin')
        self.client.force_authenticate(user=self.user_not_admin)
        self.font_1.status = STATUS_ON_REVIEW
        self.font_1.save()
        self.admin_font_relation.moderated = False
        self.admin_font_relation.save()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_font_search_no_filter_one_no_moderated_if_admin(self):
        self.client.force_authenticate(user=UserFactory(is_superuser=True, username='user_admin'))
        self.admin_font_relation.moderated = False
        self.admin_font_relation.save()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_font_search_one(self):
        response = self.client.get(self.url, data={'content_contains': 'ER'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_font_search_two(self):
        response = self.client.get(self.url, data={'content_contains': 'HE'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_font_search_three(self):
        response = self.client.get(self.url, data={'content_contains': 'T'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_font_search_empty_content_exact(self):
        response = self.client.get(self.url, data={'content_exact': 'HE'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_get_font_search_ok_content_exact(self):
        response = self.client.get(self.url, data={'content_exact': 'HER'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class FontDeleteTestCase(AuthorizeForTestsMixin, APITestCase):
    def setUp(self):
        super(FontDeleteTestCase, self).setUp()
        self.font_1 = FontFactory(owner=self.user, content='THE')
        self.admin_font_relation = AdminFontRelationFactory(user=self.user, font=self.font_1)
        self.symbol_1 = SymbolFactory(font=self.font_1)
        self.url = reverse("fonts-detail", args=(self.font_1.pk,))

    def test_font_delete(self):
        self.assertEqual(Font.objects.all().count(), 1)
        self.assertEqual(Symbol.objects.all().count(), 1)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Font.objects.all().count(), 0)
        self.assertEqual(Symbol.objects.all().count(), 0)

    def test_font_delete_not_owner(self):
        self.client.force_authenticate(user=UserFactory(username='user_2'))
        self.assertEqual(Font.objects.all().count(), 1)
        self.assertEqual(Symbol.objects.all().count(), 1)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Font.objects.all().count(), 1)
        self.assertEqual(Symbol.objects.all().count(), 1)


class UploadImageTestCase(AuthorizeForTestsMixin, APITestCase):
    def setUp(self):
        super(UploadImageTestCase, self).setUp()
        self.url = reverse("font-upload", args=('test_file.jpg',))
        self.test_file = open('fonts/tests/test_file.jpg', 'rb').read()

    def test_upload_image(self):
        response = self.client.post(self.url, {'image': self.test_file}, format='multipart')
        image_obj = ImageObj.objects.get()
        self.assertEqual(response.data, ImageObjOutSerializer(image_obj).data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        ImageObj.objects.all()[0].image_original.delete()


class FontsCountTestCase(AuthorizeForTestsMixin, APITestCase):
    def setUp(self):
        super(FontsCountTestCase, self).setUp()
        self.font_1 = FontFactory(owner=self.user, content='THE')
        self.font_2 = FontFactory(owner=self.user, content='HER')
        self.symbol_1 = SymbolFactory(font=self.font_1)
        self.symbol_2 = SymbolFactory(font=self.font_1)
        self.symbol_3 = SymbolFactory(font=self.font_2)
        self.url = reverse("fonts-count-list")

    def test_get_fonts_count(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, FontCountSerializer(data={'count': 2}).initial_data)

    def test_get_fonts_count_filter(self):
        response = self.client.get(self.url, data={'content_exact': 'HER'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, FontCountSerializer(data={'count': 1}).initial_data)
