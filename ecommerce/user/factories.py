import datetime

import factory
from django.contrib.auth.models import User

from ecommerce.user.models import Customer
from ecommerce.user.models.user_profile import UserProfile


class UserFactory(factory.DjangoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker(