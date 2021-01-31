"""Client Model."""

# Django
from django.db import models

# Utilities
from utils.models import ConcretosModel


class Client(ConcretosModel):

    name = models.TextField(max_length=500, blank=True)
    social_reason = models.TextField(max_length=500, blank=True)
    address = models.TextField(max_length=500, blank=True)
    country = models.TextField(max_length=500, blank=True)
    city = models.TextField(max_length=500, blank=True)
    postal_code = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class ClientContact(ConcretosModel):

    name = models.TextField(max_length=500, blank=True)
    last_name = models.TextField(max_length=500, blank=True)
    phone = models.IntegerField()
    email = models.TextField(max_length=500, blank=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
