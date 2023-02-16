from django.contrib import admin
from .models import Realisateur, Scenario, Film, Acteur, Jouer, Client, Emprunter


# Register your models here.
admin.site.register(Realisateur)
admin.site.register(Scenario)
admin.site.register(Film)
admin.site.register(Acteur)
admin.site.register(Jouer)
admin.site.register(Client)
admin.site.register(Emprunter)
