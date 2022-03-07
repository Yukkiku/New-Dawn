from unittest import TestCase

from ecommerce.product.factories import ProductFactory, CategoryFactory
from ecommerce.product.models import Category


class TestCategory(TestCase):
    def setUp(self) -> None:
      