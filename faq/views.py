from django.shortcuts import render

from .models import FAQ
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FaqSerializer

# Create your views here.

class FaqViewSet(viewsets.ModelViewSet):

    queryset = FAQ.objects.all()
    serializer_class = FaqSerializer
    # permission_classes = [permissions.IsAuthenticated]