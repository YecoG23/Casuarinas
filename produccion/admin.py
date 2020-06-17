from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Buzon, RedSecundaria

# Register your models here.
admin.site.register(Buzon, admin.ModelAdmin)
admin.site.register(RedSecundaria, admin.ModelAdmin)