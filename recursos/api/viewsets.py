from rest_framework.viewsets import ModelViewSet
from .serializers import RecursosSerializer
from recursos.models import Recursos

class RecursosViewSet(ModelViewSet):
    queryset = Recursos.objects.all() #como se fosse o SQL -> Pelo models
    serializer_class = RecursosSerializer #serializa em JSON
