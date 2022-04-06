import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from ecommerce.product.factories import ProductFactory
from ecommerce.product.models import Product


class TestProductViewSet(APITestCase):
    client =