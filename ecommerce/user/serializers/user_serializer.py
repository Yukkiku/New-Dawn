from rest_framework import serializers


def generic_serializer(cls):
    class BaseSerializer(serializers.Mo