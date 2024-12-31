from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.


class RsvpViewSet(ModelViewSet):
    queryset = Rsvp.objects.all()
    serializer_class = RsvpSerializer
