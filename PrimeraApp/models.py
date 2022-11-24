from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class Experiencias(models.Model):

    evaluaciones = (
        ("malo", 'Bad'),
        ("normal", 'Normal'),
        ("bueno", 'Good'),
    )
    evaluacion = models.CharField(max_length = 6, choices = evaluaciones)
    
    mensaje = models.CharField(max_length = 300, blank=False)

    fecha = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return(f"{self.evaluacion} {self.mensaje} ")


    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"



class Profile(models.Model):
    tiene_experiencia = models.BooleanField(default=None)

    def __str__(self):
        return(f"este es el usuario {self.usuario} ")

class Cursos(models.Model):
    título = models.CharField(max_length=50)
    subtítulo = models.CharField(max_length=150)
    cuerpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='fotos', blank=True, null=True)

    def __str__(self):
        return (f"{self.título}")
    