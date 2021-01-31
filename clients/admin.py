"""Client models admin."""

# Django
from django.contrib import admin

# Models
from clients.models import Client, ClientContact

admin.site.register(Client)
admin.site.register(ClientContact)
