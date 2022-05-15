from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ecommerce.product.models import Product


class ProductViewSet(ModelViewSe