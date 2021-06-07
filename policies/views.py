from django.shortcuts import render

from .models import Policy
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import Policy_Serializer

# Create your views here.

class Policy_ViewSet(viewsets.ModelViewSet):

    queryset = Policy.objects.all()
    serializer_class = Policy_Serializer
    # permission_classes = [permissions.IsAuthenticated]

""" class Placement_Policy_ViewSet(viewsets.ModelViewSet):

    queryset = Policy.objects.all()
    serializer_class = Placement_Policy_Serializer
    # permission_classes = [permissions.IsAuthenticated]     """