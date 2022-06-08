from rest_framework import serializers
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.models.session import Session
from swoleapi.serializers.user_serializer import SwoleUserSerializer

class SessionSerializer(serializers.ModelSerializer):
    """JSON Serializer for Sessions"""
    user = SwoleUserSerializer()
    
    class Meta:
        model = Session
        fields = ("id", "date", "rating", "user", "exercisesInSession")
        depth = 1
        
class ExerciseInSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise_In_Session
        fields = ("id", 'exercise','session','set_number', 'reps', 'load')