from rest_framework import viewsets, filters, status
import django_filters.rest_framework
from .models import Imovel
from .serializers import ImovelSerializer
from rest_framework.response import Response

class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'message': 'Imóvel criado com sucesso', 'data': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
        except:
            return Response({'message': 'Erro ao criar imóvel'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({'message': 'Atualização realizada com sucesso', 'data': serializer.data})
        except:
            return Response({'message': 'Imóvel não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({'message': 'Imóvel apagado com sucesso'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Imóvel não encontrado'}, status=status.HTTP_404_NOT_FOUND)