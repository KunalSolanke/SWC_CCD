from rest_framework import serializers
from lifeatiitg.models import Contents

class ContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = ['title','description','link']


