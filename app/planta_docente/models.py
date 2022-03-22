from django.db import models

# Create your models here.

class Area(models.Model):
    numero = models.SmallIntegerField()
    nombre = models.CharField(max_length=100, verbose_name="Nombre Área")

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"
        ordering = ['numero']

    def __str__(self):
        return self.nombre