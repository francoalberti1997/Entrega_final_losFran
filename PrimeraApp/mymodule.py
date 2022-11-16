
from django.contrib.auth.models import User


class Usuarios_module(User):
   def filter(campo, dato):
        busqueda = User.objects.filter(campo, dato)
        if busqueda is not None:
            return busqueda

