import factory

from ecommerce.product.models import (
    Product,
    Book,
    EBook,
    Category,
)
from ecommerce.product.models.product_variation import ProductVariation


class CategoryFactory(fac