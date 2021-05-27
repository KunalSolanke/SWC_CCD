from django.shortcuts import render

from .models import Head_of_center , Faculty_members , Department_reps ,Ccd_office_cont ,Admin_staff ,Contacts ,Placement_coordinators ,Intern_coordinators
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import Head_of_centerSerializer, Faculty_membersSerializer,Department_repsSerializer,Ccd_office_contSerializer,Admin_staffSerializer,ContactsSerializer,Placement_coordinatorsSerializer,Intern_coordinatorsSerializer

# Create your views here.

class Head_of_centerViewSet(viewsets.ModelViewSet):

    queryset = Head_of_center.objects.all()
    serializer_class = Head_of_centerSerializer
    # permission_classes = [permissions.IsAuthenticated]

class Faculty_membersViewSet(viewsets.ModelViewSet):

    queryset = Faculty_members.objects.all()
    serializer_class = Faculty_membersSerializer
    # permission_classes = [permissions.IsAuthenticated]

class Department_repsViewSet(viewsets.ModelViewSet):

    queryset = Department_reps.objects.all()
    serializer_class = Department_repsSerializer
    # permission_classes = [permissions.IsAuthenticated]

class Ccd_office_contViewSet(viewsets.ModelViewSet):

    queryset = Ccd_office_cont.objects.all()
    serializer_class = Ccd_office_contSerializer
    # permission_classes = [permissions.IsAuthenticated]

class Admin_staffViewSet(viewsets.ModelViewSet):

    queryset = Admin_staff.objects.all()
    serializer_class = Admin_staffSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ContactsViewSet(viewsets.ModelViewSet):

    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    # permission_classes = [permissions.IsAuthenticated]

class Placement_coordinatorsViewSet(viewsets.ModelViewSet):

    queryset = Placement_coordinators.objects.all()
    serializer_class = Placement_coordinatorsSerializer
    # permission_classes = [permissions.IsAuthenticated]

class Intern_coordinatorsViewSet(viewsets.ModelViewSet):

    queryset = Intern_coordinators.objects.all()
    serializer_class = Intern_coordinatorsSerializer
    # permission_classes = [permissions.IsAuthenticated]