from rest_framework import serializers
from home.models import About,CampusRecuitment,Acknowledgement

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['about']

class CampusRecuitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampusRecuitment
        fields = ['title','content']

class AcknowledgementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acknowledgement
        fields = ['title','image','content','link']

