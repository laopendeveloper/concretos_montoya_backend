"""Clients views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from clients.serializers.clients import ClientModelSerializer, ContactModelSerializer

# Models
from clients.models import Client, ClientContact


class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer


class ContactViewSet(viewsets.ModelViewSet):

    queryset = ClientContact.objects.all()
    serializer_class = ContactModelSerializer

    # def retrieve(self, request, *args, **kwargs):
    #    """Add extra data to the response."""
    #    response = super(ContactViewSet, self).retrieve(request, *args, **kwargs)
    #    clients = Client.objects.filter(
    #        client=request.client
    #    )
    #    data = {
    #        'contact': response.data,
    #        'client': ClientModelSerializer(clients, many=True).data
    #    }
    #    response.data = data
    #    return response
