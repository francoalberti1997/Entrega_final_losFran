from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Experiencias(models.Model):

    evaluaciones = (
        ("malo", 'Bad'),
        ("normal", 'Normal'),
        ("bueno", 'Good'),
    )
    evaluacion = models.CharField(max_length = 6, choices = evaluaciones)
    
    mensaje = models.CharField(max_length = 300, blank=False)

   

    def __str__(self):
        return(f"{self.evaluacion}")


    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"
#Clase CRUD que tiene todos los métodos CRUD. Aplicables a cualquier objeto en la página como usuario, experiencias, Cursos
class Crud(models.Model):
    def __init__(self, objeto):
        self.objeto = objeto
    
    def __str__(self):
        return self.print()

    def create(self):
        return self.create()
    
    def retrieve(self, attr):
        return self.retrieve(attr)

    def update(self, attr, new_attr):
        self.attr = new_attr
        return (f"el atributo : {self.attr} cambió a {new_attr}")

    def delete_obj(self):
        return self.delete()
    
class Usuarios(User):
    def __init__(self, name, apellido):
        self.apellido = apellido
        self.name = name

    def __str__(self):
        return(f"esta es la clase usuarios. {self.name}  {self.apellido} ")


Franco = Usuarios("Franco", "Alberti")

print(Franco, "holdsdsda")

print("Sas")
