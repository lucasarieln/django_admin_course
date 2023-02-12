from .serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao
from rest_framework.viewsets import ModelViewSet

class AvaliacaoViewSet(ModelViewSet):
    serializer_class = AvaliacaoSerializer
    queryset = Avaliacao.objects.all()
