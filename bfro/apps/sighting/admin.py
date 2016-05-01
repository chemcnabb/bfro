from django.contrib import admin

# Register your models here.
from django.contrib import admin
from bfro.apps.sighting.models import Sighting



class SightingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sighting, SightingAdmin)