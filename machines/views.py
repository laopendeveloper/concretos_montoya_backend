"""Machine views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from machines.serializers import MachineModelSerializer, MachineTypeModelSerializer, MachineFilesModelSerializer

# Models
from machines.models import Machine, MachineType, MachineFiles


class MachineTypeViewSet(viewsets.ModelViewSet):

    queryset = MachineType.objects.all()
    serializer_class = MachineTypeModelSerializer


class MachineFilesViewSet(viewsets.ModelViewSet):

    queryset = MachineFiles.objects.all()
    serializer_class = MachineFilesModelSerializer


class MachineViewSet(viewsets.ModelViewSet):

    queryset = Machine.objects.all()
    serializer_class = MachineModelSerializer

    # def retrieve(self, request, *args, **kwargs):
    #    """Add extra data to the response."""
    #    response = super(MachineViewSet, self).retrieve(request, *args, **kwargs)
    #    machine_type = MachineType.objects.filter(
    #        machine=request.machine
    #    )
    #    data = {
    #        'machine': response.data,
    #        'type': MachineTypeModelSerializer(machine_type, many=True).data
    #    }
    #    response.data = data
    #    return response

