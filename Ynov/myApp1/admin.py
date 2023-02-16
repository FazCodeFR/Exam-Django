from django.contrib import admin
from .models import Realisateur, Scenario, Film, Acteur


# Register your models here.
admin.site.register(Realisateur)
admin.site.register(Scenario)
admin.site.register(Film)
admin.site.register(Acteur)
