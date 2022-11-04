from multiprocessing.context import assert_spawning
from django.contrib import admin
from PrimeraApp.models import Experiencias, Usuarios
# Register your models here.



admin.site.register(Experiencias)
admin.site.register(Usuarios)