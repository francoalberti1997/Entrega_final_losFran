from tabnanny import verbose
from django.db import models

# Create your models here.

class Experiencias(models.Model):

    evaluaciones = (
        ("malo", 'Bad'),
        ("normal", 'Normal'),
        ("bueno", 'Good'),
    )
    evaluacion = models.CharField(max_length = 6, choices = evaluaciones)
    
    mensaje = models.CharField(max_length = 300, blank=True)

    def __str__(self):
        return(f"{self.evaluacion}")


    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"

    