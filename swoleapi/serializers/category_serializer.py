from rest_framework import serializers
from swoleapi.models.category import Category



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ("id", 'label')
