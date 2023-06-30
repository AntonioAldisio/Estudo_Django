from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from api.views import AnuncioViewSet
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
router.register('anuncios', AnuncioViewSet, basename='anuncios')

schema_view = get_swagger_view(
    openapi.Info(
        title="Documentação da API",
        default_version='v1',
        description="Documentação da API Anuncios",
        contact=openapi.Contact(email="antonioaldisio@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


@swagger_auto_schema(methods=['get', 'post', 'put'])
def filtered_schema_view(request):
    schema = schema_view().get_schema(request=request)
    paths = schema['paths']
    filtered_paths = {}

    for path, path_info in paths.items():
        filtered_operations = {
            method: operation
            for method, operation in path_info.items()
            if method in ['get', 'post', 'put']  # Defina aqui as operações permitidas
        }
        if filtered_operations:
            filtered_paths[path] = filtered_operations

    schema['paths'] = filtered_paths
    return schema


urlpatterns = [
    path('api/', include(router.urls)),
    path('swagger/', schema_view, name='schema-swagger-ui'),
]
