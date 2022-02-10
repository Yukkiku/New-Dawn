from django.db import models

from ecommerce.product.models import Product


class ProductVariation(models.Model):
    title = models.CharField(max_length=100)