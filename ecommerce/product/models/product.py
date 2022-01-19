from django.db import models
from rest_framework import serializers

from ecommerce.product.models.category import Category


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerFie