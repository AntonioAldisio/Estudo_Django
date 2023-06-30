from rest_framework import viewsets, filters
import django_filters.rest_framework
from .models import Anuncio
from .serializers import AnunciosSerializer
from rest_framework.response import Response


class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnunciosSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'

    def get(self, request, *args, **kwargs):
        queryset = Anuncio.objects.all()
        serializer = AnunciosSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AnunciosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Anúncio criado com sucesso', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        try:
            instance = Anuncio.objects.get(pk=pk)
        except Anuncio.DoesNotExist:
            return Response({'message': 'Anúncio não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AnunciosSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Atualização realizada com sucesso', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Anuncio.objects.all()
