import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from ecommerce.product.factories import ProductFactory
from ecommerce.product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self) -> None:
        self.product = ProductFactory()

    def test_get_all_books(self):
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = json.loads(response.content)[0]

        self.assertEqual(product_data['title'], self.product.title)
        self.asse