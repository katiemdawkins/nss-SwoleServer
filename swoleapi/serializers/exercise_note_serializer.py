from rest_framework import serializers
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.models.exercise_note import Exercise_Note
from swoleapi.models.note_tag import Note_Tag
from swoleapi.serializers.user_serializer import UserNoEmailSerializer


class ExerciseInSessionForNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise_In_Session
        fields = ('id', 'exercise', )

class ExerciseNoteSerializer(serializers.ModelSerializer):
    
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