from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class ProdutoViewSet(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Produto.objects.all()
        serializer = ProdutoSerializer(queryset, many=True)
        return Response(serializer.data)

       

