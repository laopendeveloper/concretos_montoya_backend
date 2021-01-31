"""Machine models admin."""

# Django
from django.contrib import admin

# Models
from machines.models import Machine, MachineType, MachineFiles

admin.site.register(Machine)
admin.site.register(MachineType)
admin.site.register(MachineFiles)
