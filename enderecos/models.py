from django.db import models


class Endereco(models.Model):
    linha1 = models.CharField(max_length=255)
    linha2 = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=128)
    estado = models.CharField(max_length=128)
    pais = models.CharField(max_length=128)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.linha1}, {self.cidade}"
    
    class Meta:
        verbose_name_plural = "Endereços"