from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Rsvp)
class RsvpAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'attendance', 'message']
