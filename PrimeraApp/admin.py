from multiprocessing.context import assert_spawning
from django.contrib import admin
from PrimeraApp.models import Experiencias, Profile



admin.site.register(Experiencias)
admin.site.register(Profile)
