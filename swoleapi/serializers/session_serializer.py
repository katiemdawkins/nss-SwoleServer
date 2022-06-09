from rest_framework import serializers
from swoleapi.models import exercise_in_session
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.models.session import Session
from swoleapi.serializers.user_serializer import SwoleUserForSessionSerializer


class ExerciseInSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise_In_Session
        fields = ("id", 'exercise','session','set_number', 'reps', 'load')
        

        
class SessionSerializer(serializers.ModelSerializer):
    """JSON Serializer for Sessions"""
    user = SwoleUserForSessionSerializer()
   # exercisesInSession = ExerciseInSessionSerializer()
    
    class Meta:
        model = Session
        fields = ("id", "date", "rating", "user", "exercisesInSession")
        depth = 1
        