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

    curso = models.ForeignKey("Curso", on_delete=models.CASCADE,)
    
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
    



class Curso(models.Model):
    lista_nombre = (("Basic","Basico"), ("Intermediate","Intermedio"), ("Advanced","Avanzado"))
    lista_duracion = ((6,"6 meses"), (4,"4 meses"), (3,"3 meses"))
    
    nombre = models.CharField(max_length=50, choices=lista_nombre)
    duracion = models.CharField(max_length=50, choices=lista_duracion)

    def __str__(self):
        return (f" {self.nombre} ")    

