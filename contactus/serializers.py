from .models import Head_of_center , Faculty_members , Department_reps ,Ccd_office_cont ,Admin_staff ,Contacts ,Placement_coordinators ,Intern_coordinators
from rest_framework import serializers

class Head_of_centerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Head_of_center
        fields = '__all__'
        
class Faculty_membersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty_members
        fields = '__all__'

class Department_repsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department_reps
        fields = '__all__'

class Ccd_office_contSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ccd_office_cont
        fields = '__all__'

class Admin_staffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin_staff
        fields = '__all__'

class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

class Placement_coordinatorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Placement_coordinators
        fields = '__all__'

class Intern_coordinatorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intern_coordinators
        fields = '__all__'