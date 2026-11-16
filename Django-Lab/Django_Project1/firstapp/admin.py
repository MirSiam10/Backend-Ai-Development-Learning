from django.contrib import admin  # type: ignore[import-untyped]
from .models import Reservation

# Register your models here.
admin.site.register(Reservation)



