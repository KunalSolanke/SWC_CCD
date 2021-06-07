from .models import Policy
from rest_framework import serializers

class Policy_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'
        
""" class Placement_Policy_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'    """     