from django.test import TestCase

from ecommerce.product.factories import EBookFactory, BookFactory
from ecommerce.product.models import EBook, Book


class TestGenericProductSerializer(TestCase):
    def setUp(self) -> None:
        self.e_book = EBookFactory()
        self.book = BookFactory()

    def test_get_e_book_serializer(self):
        serializer_class = EBook.get_serializer()
        serializer_data = serializer_class(self.e_book).data
  