from django.db import models

from ecommerce.product.models.product import Product


class Book(Product):
    weight = 