from rest_framework import serializers
from swoleapi.models.exercise_in_session import Exercise_In_Session

class CreateExerciseInSession(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise_In_Session
        fields = ("id","exercise", "session", "set_number", "load", "reps")