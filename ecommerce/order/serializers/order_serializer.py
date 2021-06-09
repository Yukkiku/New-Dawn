
from rest_framework import serializers

from ecommerce.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):

        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('order', '') if request else None