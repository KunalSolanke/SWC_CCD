from .models import FAQ
from rest_framework import serializers

class FaqSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
        
