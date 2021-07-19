from django.contrib import admin

from .models import City, Reservations


admin.site.register(City)
admin.site.register(Reservations)