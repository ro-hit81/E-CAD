from django.contrib import admin
from django.contrib.gis import admin
from .models import Parcel, Building, Transportation, Hydro

# Register your models here.


admin.site.register(Parcel, admin.GeoModelAdmin)
admin.site.register(Building, admin.GeoModelAdmin)
admin.site.register(Transportation, admin.GeoModelAdmin)
admin.site.register(Hydro, admin.GeoModelAdmin)