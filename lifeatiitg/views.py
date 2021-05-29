from django.shortcuts import render
from rest_framework import viewsets
from lifeatiitg.models import Contents
from lifeatiitg.serializers import ContentsSerializer
# Create your views here.

class ContentsViewSet(viewsets.ModelViewSet):
    serializer_class = ContentsSerializer
    queryset = Contents.objects.all()

