from django.urls import path, include
from rest_framework import routers

from ecommerce.product import viewsets

router = routers.SimpleRouter(