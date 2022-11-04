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


    def __str__(self):
        return(f"{self.evaluacion}")


    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"

class Usuarios(models.Model):
    experiencia =  models.ForeignKey(Experiencias, on_delete=models.CASCADE, null=True) #quiero que se registre solo con nombre, apellido y contrase. El mensaje y experiencia los pasará el usuario luego que ingrese
    nombre = models.CharField(max_length = 25)
    apellido = models.CharField(max_length = 25)
    contraseña = models.CharField(max_length = 25)
    fecha = models.DateField(auto_now=True)
    mensaje = models.CharField(max_length = 300, blank=True)#quiero que se registre solo con nombre, apellido y contrase. El mensaje y experiencia los pasará el usuario luego que ingrese

    def __str__(self) -> str:
        return (f" {self.nombre}" + " " + f" {self.apellido} ")
    

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"