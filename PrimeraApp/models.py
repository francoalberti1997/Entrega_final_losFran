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
    experiencias = models.ForeignKey(Experiencias, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    tiene_experiencia = models.BooleanField(default=False)


class Curso(models.Model):
    lista_nombre = (("Basic","Basico"), ("Intermediate","Intermedio"), ("Advanced","Avanzado"))
    lista_duracion = (("6","6 meses"), ("4","4 meses"), ("3","3 meses"))
    nombre = models.CharField(max_length=50, choices=lista_nombre)
    duracion = models.CharField(max_length=50, choices=lista_duracion)#problema, quiero que el usuario tilde casilla con opciones relativas a lista_nombre

    def __str__(self):
        return (f" {self.nombre} ")    


