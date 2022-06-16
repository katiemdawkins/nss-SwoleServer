"""View for handling ExerciseNote requests"""
from argparse import Action
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from swoleapi.models.exercise_note import Exercise_Note
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.models.tag import Tag
from swoleapi.serializers.exercise_note_serializer import CreateExerciseNoteSerializer, ExerciseNoteSerializer, CreateNoteTagSerializer

class ExerciseNoteView(ViewSet):
    """ExerciseNote View"""
    
    def retrieve(self, request, pk):
        """Handle GET Request for Single Exercise Note"""
        try:
            exercise_note= Exercise_Note.objects.get(pk=pk)
            serializer = ExerciseNoteSerializer(exercise_note)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Exercise_Note.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """handel GET requests for all Exercise Notes"""
        exercise_notes= Exercise_Note.objects.all()
        serializer = ExerciseNoteSerializer(exercise_notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    def create(self, request):
        """Post Request for Exercise Note"""
        exercise_in_session = Exercise_In_Session.objects.get(pk=request.data['exercise_in_session'])
        serializer = CreateExerciseNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(exercise_in_session=exercise_in_session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

    ## Custom action creating Note Tags
    @action(methods=['post'],detail=True)
    def addNoteTags(self, request, pk):
        try:
            exercise_note = Exercise_Note.objects.get(pk=pk)
            tag = Tag.objects.get(pk=request.data['tag'])
            exercise_note.tags.add(tag)
            return Response({'message': 'Note tags updated'}, status=status.HTTP_204_NO_CONTENT)
        except Exercise_Note.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            