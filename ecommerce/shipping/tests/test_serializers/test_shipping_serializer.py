from django.test import TestCase

from ecommerce.shipping.factories import ShippingFactory
from ecommerce.shipping.serializers.shipping_serializer import ShippingSerializer


class TestShippingSerializer(TestCase):
    def setUp(self) -> None:
        self.shipping = ShippingFactory()
        self.shipping_serializer = ShippingSerializer(self.shipping)

    def test_get_shippi