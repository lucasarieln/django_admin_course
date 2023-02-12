from rest_framework.serializers import ModelSerializer
from recursos.models import Recursos

class RecursosSerializer(ModelSerializer):
    class Meta:
        model = Recursos
        fields = ['id', 'nome', 'description', 'horario_funcionamento', 'idade_minima']