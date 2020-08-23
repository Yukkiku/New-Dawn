import factory

from ecommerce.cart.models import CartItem
from ecommerce.cart.models.cart import Cart
from ecommerce.product.factories import ProductVariationFactory
from ecommerce.user.factories import UserProfileFactory


class CartFactory(factory.DjangoModelFactory):
    u