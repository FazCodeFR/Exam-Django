from django.contrib import admin
from .models import Dirigeant, Magasin, Meuble


# Register your models here.
admin.site.register(Dirigeant)
admin.site.register(Magasin)
admin.site.register(Meuble)
