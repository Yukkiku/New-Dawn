
from django.test import TestCase

from ecommerce.order.constants import SEA, AIR, GROUND
from ecommerce.shipping.factories import Shipping, ShippingFactory


class ShippingTypeTestCase(TestCase):
    def setUp(self):
        self.sea = ShippingFactory