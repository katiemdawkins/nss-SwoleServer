from rest_framework import serializers
from swoleapi.models.exercise import Exercise
from swoleapi.models.session import Session
from swoleapi.serializers.user_serializer import SwoleUserSerializer



class ExerciseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise
        fields = ("id", 'name','description','image_url', 'body_part', 'category')
        depth=1
        