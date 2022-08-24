
from django.test import TestCase

from ecommerce.order.constants import SEA, AIR, GROUND
from ecommerce.shipping.factories import Shipping, ShippingFactory


class ShippingTypeTestCase(TestCase):
    def setUp(self):
        self.sea = ShippingFactory(weight=10, cost=2, shipment_type=SEA)
        self.ground = ShippingFactory(weight=10, cost=1, shipment_type=GROUND)
        self.air = ShippingFactory(weight=10, cost=4, shipment_type=AIR)

    def test_get_sea_cost(self):
        sea = Shipping.objects.get(id=self.sea.id)
       