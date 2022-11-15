from django.contrib import admin

from reservations.models import Reservations, Room

# Register your models here.
admin.site.register(Reservations)
admin.site.register(Room)