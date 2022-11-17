from multiprocessing.context import assert_spawning
from django.contrib import admin
from PrimeraApp.models import Experiencias, Curso, Usuarios



admin.site.register(Experiencias)
admin.site.register(Curso)
admin.site.register(Usuarios)

