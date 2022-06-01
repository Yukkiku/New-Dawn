import factory

from ecommerce.shipping.models import Shipping


class ShippingFactory(factory.DjangoModelFactory):
    cost = factory.Iterator([1,