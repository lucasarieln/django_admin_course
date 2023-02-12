from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from core.api.viewsets import PontoTuristicoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from recursos.api.viewsets import RecursosViewSet

#router = routers.DefaultRouter()
#router.register(r'pontoturistico', PontoTuristicoViewSet)

router = routers.SimpleRouter()
router.register(r'ponto_turistico', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'recursos', RecursosViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((router.urls))),
]
