from django.test import TestCase

from ecommerce.product.factories import EBookFactory, BookFactory
from ecommerce.product.models import EBook, Book


class TestGenericProductSerializer(TestCase):
    def setUp(self) -> None:
        self.e_book = EBookFactory()
        self.book = BookFact