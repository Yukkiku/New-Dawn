
from django.test import TestCase

from ecommerce.product.factories import BookFactory, EBookFactory
from ecommerce.product.models import Book, EBook


class BookTestCase(TestCase):
    def setUp(se