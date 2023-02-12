from django.db import models

# Create your models here.

class Recursos(models.Model):
    nome = models.CharField(max_length=255)
    description = models.TextField()
    horario_funcionamento = models.TextField()
    idade_minima = models.IntegerField()


    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "recursos"
