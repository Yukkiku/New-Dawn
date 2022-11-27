from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        (1, 'customer'),
        (2, 'admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)