from rest_framework import serializers

from ecommerce.cart.models import Cart
from ecommerce.product.models import Product
from ecommerce.user.models import UserProfile
from ecommerce.user.serializers.user_serializer import generic_serializer


class CartSerializer(serializers.Serializer):
    user = serialize