from rest_framework import viewsets, filters
import django_filters.rest_framework
from .models import Imovel
from .serializers import ImovelSerializer

class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
