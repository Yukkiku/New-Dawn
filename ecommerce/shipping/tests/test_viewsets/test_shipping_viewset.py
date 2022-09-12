import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from ecommerce.shipping.factories import ShippingFactory


class TestShippingViewSet(APITestCase):
    client = APIClient()

    def setUp(self) -> None:
        self.shipping = ShippingFactory()

    def test_get_all_shipping(self):
        res