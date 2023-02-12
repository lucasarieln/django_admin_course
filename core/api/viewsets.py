from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.all() #como se fosse o SQL -> Pelo models
    serializer_class = PontoTuristicoSerializer #serializa em JSON


    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado = True)
