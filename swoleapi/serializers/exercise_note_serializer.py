from rest_framework import serializers
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.models.exercise_note import Exercise_Note
from swoleapi.models.note_tag import Note_Tag
from swoleapi.models.session import Session
from swoleapi.models.exercise import Exercise
from swoleapi.serializers.user_serializer import UserNoEmailSerializer

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session()
        fields = ('id', 'user')

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise()
        fields = ('id', 'name')

class ExerciseInSessionForNoteSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()
    session = SessionSerializer()
    class Meta:
        model = Exercise_In_Session
        fields = ('id', 'exercise', 'session')
        depth = 1

class ExerciseNoteSerializer(serializers.ModelSerializer):
    exercise_in_session = ExerciseInSessionForNoteSerializer()
    
    class Meta:
        model = Exercise_Note
        fields = ("id", 'description', "exercise_in_session", "tags")
        depth = 1
        
class UpdateExerciseNoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise_Note
        fields = ("id", 'description', "exercise_in_session", "tags")
        depth = 1
        
class CreateExerciseNoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise_Note
        fields = ("id", 'description', "exercise_in_session")
        depth = 1
        
class CreateNoteTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Note_Tag
        fields = ('id', 'note', 'tag')