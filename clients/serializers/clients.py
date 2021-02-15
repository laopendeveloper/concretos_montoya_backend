"""Clients serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from clients.models import Client, ClientContact


class ClientModelSerializer(serializers.ModelSerializer):
    """Client model serializer."""

    class Meta:
        """Meta class."""

        model = Client
        fields = '__all__'


class ContactModelSerializer(serializers.ModelSerializer):
    """Contact model serializer."""

    client = ClientModelSerializer

    class Meta:
        """Meta class."""

        model = ClientContact
        fields = (
            'name',
            'last_name',
            'phone',
            'email',
            'client'
        )
