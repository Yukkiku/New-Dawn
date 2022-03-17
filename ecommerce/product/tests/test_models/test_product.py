from unittest import TestCase

from ecommerce.product.factories import ProductFactory, CategoryFactory
from ecommerce.product.models import Product, ProductVariation


class TestProductVariationCase(TestCase):
    def setUp(self