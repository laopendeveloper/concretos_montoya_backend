"""Machines serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from machines.models import Machine, MachineType, MachineFiles


class MachineTypeModelSerializer(serializers.ModelSerializer):
    """Machine Type model serializer."""

    class Meta:
        """Meta class."""

        model = MachineType
        fields = '__all__'


class MachineModelSerializer(serializers.ModelSerializer):
    """Machine model serializer."""

    machine_type = MachineTypeModelSerializer

    class Meta:
        """Meta class"""

        model = Machine
        fields = (
            'name',
            'serial_number',
            'model',
            'description',
            'price',
            'machine_type'
        )


class MachineFilesModelSerializer(serializers.ModelSerializer):
    """Machine Files model serializer."""

    machine = MachineModelSerializer

    class Meta:
        """Meta class."""

        model = MachineFiles
        fields = (
            'name',
            'path',
            'file',
            'machine'
        )
