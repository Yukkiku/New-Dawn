from unittest import TestCase

from ecommerce.product.factories import ProductFactory, CategoryFactory
from ecommerce.product.models import Category


class TestCategory(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory()

    def test_get_categor