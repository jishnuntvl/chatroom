from django.contrib import admin # type: ignore

from .models import Room,Message # type: ignore

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)