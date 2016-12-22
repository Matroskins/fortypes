from django.test import TestCase

from accounts.tests.factories import UserFactory
from fonts.models import STATUS_ON_REVIEW, STATUS_PUBLIC
from fonts.tests.factories import FontFactory
from user_font_relation.tests.factories import AdminFontRelationFactory


class ModerateFontTestCase(TestCase):
    def setUp(self):
        super(ModerateFontTestCase, self).setUp()
        self.user = UserFactory(is_superuser=True, username='user_admin')
        self.font_1 = FontFactory(owner=self.user, status=STATUS_ON_REVIEW)

    def test_moderate_publish_font(self):
        relation = AdminFontRelationFactory(user=self.user, font=self.font_1, moderated=False)
        self.assertEqual(self.font_1.status, STATUS_ON_REVIEW)
        relation.moderated = True
        relation.save()
        self.font_1.refresh_from_db()
        self.assertEqual(self.font_1.status, STATUS_PUBLIC)

    def test_moderate_publish_font_not_admin(self):
        self.user_2 = UserFactory(username='user_not_admin')
        relation = AdminFontRelationFactory(user=self.user_2, font=self.font_1, moderated=False)
        self.assertEqual(self.font_1.status, STATUS_ON_REVIEW)
        relation.moderated = True
        relation.save()
        self.font_1.refresh_from_db()
        self.assertEqual(self.font_1.status, STATUS_ON_REVIEW)
