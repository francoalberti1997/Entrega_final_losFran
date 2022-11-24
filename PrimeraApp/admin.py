from multiprocessing.context import assert_spawning
from django.contrib import admin
from PrimeraApp.models import Experiencias, Profile, Cursos



admin.site.register(Experiencias)
admin.site.register(Profile)

class AdminCursos(admin.ModelAdmin):
    readonly_fields = ("id", )

admin.site.register(Cursos, AdminCursos)

