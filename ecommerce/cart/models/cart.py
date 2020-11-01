from django.db import models

from ecommerce.cart.models.cart_item import CartItem
from ecommerce.product.models.product_variation import ProductVariation
from ecommerce.user.models import UserProfile


class Cart(models.Model):
    user = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductVariation, through=CartItem)
    created_at = models.DateTimeField(a