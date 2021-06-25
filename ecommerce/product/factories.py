import factory

from ecommerce.product.models import (
    Product,
    Book,
    EBook,
    Category,
)
from ecommerce.product.models.product_variation import ProductVariation


class CategoryFactory(factory.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.DjangoModelFactory):
    price = factory.Faker('pyint')
    categories = factory.LazyAttribute(CategoryFactory)
    title =