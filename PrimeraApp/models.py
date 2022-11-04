from tabnanny import verbose
from django.db import models

# Create your models here.

class Experiencias(models.Model):
    fecha = models.DateField(auto_now=True)
    mensaje = models.CharField(max_length = 300)
    evaluaciones = (
        ("malo", 'Bad'),
        ("normal", 'Normal'),
        ("bueno", 'Good'),
    )
    evaluacion = models.CharField(max_length = 6, choices = evaluaciones)


    def __str__(self):
        return(f"{self.evaluacion}")


    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"

class Usuarios(models.Model):
    nombre = models.CharField(max_length = 25)
    apellido = models.CharField(max_length = 25)
    contraseña = models.CharField(max_length = 25)



    

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"