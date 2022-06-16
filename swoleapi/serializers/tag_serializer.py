from rest_framework import serializers
from swoleapi.models.tag import Tag



class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ("id", 'label')
        
class CreateTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ("id", 'label')