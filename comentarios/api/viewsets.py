from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all() #como se fosse o SQL -> Pelo models
    serializer_class = ComentarioSerializer #serializa em JSON