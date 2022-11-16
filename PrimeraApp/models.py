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

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f"{self.evaluacion} {self.mensaje} ")


    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"



class Usuarios(User):
    def __init__(self, name, apellido):
        self.apellido = apellido
        self.name = name
    def __str__(self):
        return(f"esta es la clase usuarios. {self.name}  {self.apellido} ")

    def retrieve(self, grupo):
        if grupo == "Admin":
            return User.objects.filter(groups='1')
        elif grupo == "Customers":
            return User.objects.filter(groups='2')
        else:
            return (f"el grupo {grupo} no forma parte los grupos de usuarios")
    



class Crud(models.Model):
    lista_de_objetos = (
        (Experiencias, "Experiencias"),
        (Usuarios, "usuarios"),
    )

    objeto = models.CharField(choices=lista_de_objetos, max_length=50)

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
    

