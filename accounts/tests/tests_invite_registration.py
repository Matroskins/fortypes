from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

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
