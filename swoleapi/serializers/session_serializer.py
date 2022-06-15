from rest_framework import serializers
from swoleapi.models import exercise_in_session
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.models.session import Session
from swoleapi.models.exercise import Exercise
from swoleapi.serializers.user_serializer import SwoleUserForSessionSerializer

class ExerciseSerializerForSession(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise
        fields = ('id', "name", "Sessions")
        depth= 1

class ExerciseInSessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise_In_Session
        fields = ("id", 'exercise', 'session','set_number', 'reps', 'load')
        depth = 1

class ExInSessSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializerForSession()
    
    class Meta:
        model = Exercise_In_Session
        fields = ('exercise', 'session', 'set_number', 'load', 'reps')
        depth = 1

class UpdateExerciseInSessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise_In_Session
        fields = ("id", 'exercise', 'session', 'set_number', 'reps', 'load')   
            
class SessionSerializer(serializers.ModelSerializer):
    """JSON Serializer for Sessions"""
    user = SwoleUserForSessionSerializer()
    Exercises_in_Session = ExInSessSerializer(many=True)
    #currentExercises = ExerciseSerializerForSession(many=True)
    
    class Meta:
        model = Session
        fields = ("id", "date", "rating", "user", "Exercises_in_Session", "is_complete", "currentExercises")
        depth = 2
    
#---------Create--------

class CreateSessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Session
        fields = ("id", "date")
        
#---------Update--------
class UpdateSessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Session
        fields = ("id", "date", "rating", "user", "is_complete")