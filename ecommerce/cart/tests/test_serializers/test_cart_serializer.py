from django.test import TestCase

from ecommerce.cart.factories import CartFactory
from ecommerce.cart.serializers.cart_serializer import CartSerializer
from ecommerce.product.factories import ProductVariationFactory


class TestCartSerializer(TestCase):
    def setUp(self) -> None:
        self.product_variation = ProductVariationFactory()
        self.cart = CartFactory(it