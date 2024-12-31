from rest_framework import serializers
from .models import *


class RsvpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rsvp
        fields = ['id', 'name', 'attendance', 'message']
