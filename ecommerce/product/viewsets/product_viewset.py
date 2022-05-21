from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ecommerce.product.models import Product


class ProductViewSet(ModelViewSet, CreateModelMixin):

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def create(self, request, *args, **kwargs):
        product_serializer = Product.get_serializer()
        serializer = product_serializer(data=request.data)

        serializer.is_v