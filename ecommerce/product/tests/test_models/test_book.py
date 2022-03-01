
from django.test import TestCase

from ecommerce.product.factories import BookFactory, EBookFactory
from ecommerce.product.models import Book, EBook


class BookTestCase(TestCase):
    def setUp(self):
        self.book = BookFactory()
        self.e_book = EBookFactory()

    def test_get_book(self):
        book