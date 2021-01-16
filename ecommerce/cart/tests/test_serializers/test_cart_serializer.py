from django.test import TestCase

from ecommerce.cart.factories import CartFactory
from ecommerce.cart.serializers.cart_serializer import CartSerializer
from ecommerce.product.factories import ProductVariationFactory


class TestCartSerializer(TestCase):
    def setUp(self) -> None:
        self.product_variation = ProductVariationFactory()
        self.cart = CartFactory(items=[self.product_variation])
        self.cart_serializer = CartSerializer(
            self.cart,
            context={
                'request': self.cart.user,
                'items': self.cart.items,
            },
  