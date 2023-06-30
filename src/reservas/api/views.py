import random
import string

from rest_framework import viewsets, filters, status
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend
from .models import Reserva
from .serializers import ReservasSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservasSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    http_method_names = ['get', 'post', 'delete']

    def generate_reservation_code(self, length=8):
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for _ in range(length))
        return code

    def create(self, request, *args, **kwargs):
        checkin_date = request.data.get('checkin_date')
        checkout_date = request.data.get('checkout_date')

        if checkin_date and checkout_date:
            if checkin_date > checkout_date:
                raise ValidationError("A data de check-in não pode ser posterior à data de check-out.")

        request.data['reservation_code'] = self.generate_reservation_code()
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(responses={200: ReservasSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(responses={200: ReservasSerializer()})
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ReservasSerializer, responses={201: ReservasSerializer()})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(responses={204: None})
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
