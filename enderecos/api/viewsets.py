from rest_framework.viewsets import ModelViewSet
from .serializers import EnderecoSerializer
from enderecos.models import Endereco

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all() #como se fosse o SQL -> Pelo models
    serializer_class = EnderecoSerializer #serializa em JSON