"""Machine models."""

# Django
from django.db import models

# Utilities
from utils.models import ConcretosModel


class MachineType(ConcretosModel):

    name = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Machine(ConcretosModel):

    name = models.TextField(max_length=500, blank=True)
    serial_number = models.TextField(max_length=500, blank=True)
    model = models.TextField(max_length=500, blank=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.FloatField()
    machine_type = models.OneToOneField('MachineType', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class MachineFiles(ConcretosModel):

    name = models.TextField(max_length=500, blank=True)
    path = models.TextField(max_length=500, blank=True)
    file = models.FileField(
        'Machine Quote',
        upload_to='machines/files/',
        blank=True,
        null=True
    )
    machine = models.ForeignKey('Machine', on_delete=models.CASCADE)
