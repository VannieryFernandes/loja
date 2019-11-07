from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework import viewsets


class ClienteViewSet(viewsets.ModelViewSet):

    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()