from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.api.viewsets import PontoTuristicoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from recursos.api.viewsets import RecursosViewSet

#router = routers.DefaultRouter()
#router.register(r'pontoturistico', PontoTuristicoViewSet)

router = routers.SimpleRouter()
router.register(r'ponto_turistico', PontoTuristicoViewSet)
router.register(r'recursos', RecursosViewSet)
router.register(r'enderecos', EnderecoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((router.urls, 'ponto_turistico'))),
    path('', include((router.urls, 'recursos'))),
    path('', include((router.urls, 'enderecos'))),
]
