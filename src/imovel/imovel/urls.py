from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ImovelViewSet

router = DefaultRouter()
router.register('imoveis', ImovelViewSet, basename='imovel')

urlpatterns = [
    path('api/', include(router.urls)),
]
