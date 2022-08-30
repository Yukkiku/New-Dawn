from django.test import TestCase

from ecommerce.shipping.factories import ShippingFactory
from ecommerce.shipping.serializers.shipping_serializer import ShippingSerializer


class TestShippingSerializer(TestCase):
    def 