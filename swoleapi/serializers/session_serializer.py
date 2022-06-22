from rest_framework import serializers
from swoleapi.models import exercise_in_session
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.models.session import Session
from swoleapi.models.exercise import Exercise
from swoleapi.serializers.user_serializer import SwoleUserForSessionSerializer

# class EISForList(serializers.ModelSerializer):
#     class Meta:
#         model = Exercise_In_Session
#         fields = ("id",'session','set_number', 'reps', 'load', "date")
#         depth = 1

class ExerciseSerializerForSession(serializers.ModelSerializer):
    #Sessions = 
    class Meta:
        model = Exercise
        fields = ('id', "name", "Sessions")
        depth= 1

class ExerciseInSessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise_In_Session
        fields = ("id", 'exercise', 'session','set_number', 'reps', 'load')
        depth = 1
        
class SessionForExInSessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Session
        fields = ('id', )
        depth = 1

class ExInSessSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializerForSession()
    session = SessionForExInSessSerializer()
    
    class Meta:
        model = Exercise_In_Session
        fields = ('exercise', 'session', 'set_number', 'load', 'reps')
        depth = 1

class UpdateExerciseInSessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise_In_Session
        fields = ("id", 'exercise', 'session', 'set_number', 'reps', 'load')   

##### for listing user's sessions           
class SessionSerializer(serializers.ModelSerializer):
    """JSON Serializer for Sessions"""
    user = SwoleUserForSessionSerializer()
    Exercises_in_Session = ExInSessSerializer(many=True)
    
    class Meta:
        model = Session
        fields = ("id", "date", "rating", "user", "is_complete", "Exercises_in_Session", "currentExercises")
        depth = 2
 
###Abbreviated Session Serializer
class ShortSessionSerializer(serializers.ModelSerializer):
    """JSON Serializer for Sessions"""
    
    class Meta:
        model = Session
        fields = ("id", "date", "rating", "user", "is_complete", 'averageRating' )

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