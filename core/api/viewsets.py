from rest_framework import viewsets
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    queryset = PontoTuristico.objects.all() #como se fosse o SQL -> Pelo models
    serializer_class = PontoTuristicoSerializer #serializa em JSON