from typing import ClassVar
from django.shortcuts import render
from rest_framework import viewsets
from home.models import About,CampusRecuitment,Acknowledgement
from home.serializers import AboutSerializer,CampusRecuitmentSerializer,AcknowledgementSerializer
# Create your views here.

class AboutViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()

class CampusRecuitmentViewSet(viewsets.ModelViewSet):
    serializer_class = CampusRecuitmentSerializer
    queryset = CampusRecuitment.objects.all()

class AcknowledgementViewSet(viewsets.ModelViewSet):
    serializer_class = AcknowledgementSerializer
    queryset = Acknowledgement.objects.all()





