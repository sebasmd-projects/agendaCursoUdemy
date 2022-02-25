from django.contrib import admin
from .models import Persona, Reunion, Hobby

# Register your models here.
admin.site.register(Persona)
admin.site.register(Reunion)
admin.site.register(Hobby)