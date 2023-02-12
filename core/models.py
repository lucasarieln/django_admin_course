from django.db import models
from recursos.models import Recursos
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


# Create your models here.

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=255)
    description = models.TextField()
    aprovado = models.BooleanField(default=False)
    recursos = models.ManyToManyField(Recursos) #many to many fields
    comentarios = models.ManyToManyField(Comentario) #many to many fields
    avaliacoes = models.ManyToManyField(Avaliacao) #many to many fields
    Endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True
        )

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Pontos turísticos"
