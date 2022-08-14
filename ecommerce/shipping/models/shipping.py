
from django.db import models

from ecommerce.order.constants import (
    GROUND,
    AIR,
    SEA,
)


class Shipping(models.Model):
    name = models.CharField(max_length=30)
    weight = models.PositiveIntegerField(null=True, default=0)

    SHIPMENT_TYPE_CHOICES = [
        (GROUND, 'GROUND'),
        (AIR, 'AIR'),
        (SEA, 'SEA'),
    ]

    shipment_type = models.CharField(
        max_length=30,
        choices=SHIPMENT_TYPE_CHOICES,
    )

    cost = models.PositiveIntegerField(
        help_text='in cents',