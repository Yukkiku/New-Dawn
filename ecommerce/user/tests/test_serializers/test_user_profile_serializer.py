from django.test import TestCase

from ecommerce.user.factories import UserProfileFactory
from ecommerce.user.models import UserProfile
from ecommerce.user.serializers.user_serializer import generic_serializer


class TestUserProfileSerializer(TestCase):
    def setUp(self) -> None:
        self.user = UserProfileFactory()
        self.user_profile_serializer = generic