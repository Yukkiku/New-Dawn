import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from ecommerce.user.factories import UserProfileFactory


class TestUserProfileViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserProfileFactory()

    def test_get_all_users(self):
        response = self.client.get(
            reverse('user-list', kwargs={'version'