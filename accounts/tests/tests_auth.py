from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.tests.factories import UserFactory
from core.tests import AuthorizeForTestsMixin
from invite.models import Invite
from invite.tests.factories import InviteFactory


class RegistrationTestCase(APITestCase):
    def setUp(self):
        super(RegistrationTestCase, self).setUp()
        self.invite = InviteFactory()
        self.url = reverse("invite-registration")

    def test_registration_by_invite_code(self):
        self.data = {
            "email": "test@example.com",
            "password": "saagrerr",
            "invite_code": 'INVTCD',
        }
        invite = Invite.objects.get()
        self.assertFalse(invite.used)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get()
        self.assertEqual(user.email, "test@example.com")
        invite.refresh_from_db()
        self.assertTrue(invite.used)
        self.assertEqual(invite.user_who_used, user)

    def test_registration_by_wrong_invite_code(self):
        self.data = {
            "email": "test@example.com",
            "password": "saagrerr",
            "invite_code": 'ABSDEF',
        }
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'invite_code': ['Wrong invite code']})

    def test_registration_and_login(self):
        self.data = {
            "email": "test@example.com",
            "password": "saagrerr",
            "invite_code": 'INVTCD',
        }
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.url = '/rest-auth/login/'
        self.data = {
            "email": "test@example.com",
            "password": "saagrerr", }
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['key'])


class AuthTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.email = 'test@user.com'
        self.password = 'saagrerr'
        self.user = UserFactory(email=self.email)
        self.user.set_password(self.password)
        self.user.save()

    def test_auth(self):
        user = authenticate(email=self.email, password=self.password)
        self.assertEqual(user, self.user)

    def test_login(self):
        self.url = '/rest-auth/login/'
        self.data = {
            "email": self.email,
            "password": self.password}
        response = self.client.post(self.url, self.data)
        self.assertTrue(response.data['key'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user.is_authenticated())

    def test_logout(self):
        self.url = '/rest-auth/logout/'
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user.is_authenticated())
