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
from swoleapi.serializers.exercise_note_serializer import CreateExerciseNoteSerializer, ExerciseNoteSerializer, CreateNoteTagSerializer, UpdateExerciseNoteSerializer

class ExerciseNoteView(ViewSet):
    """ExerciseNote View"""
    
    def retrieve(self, request, pk):
        """Handle GET Request for Single Exercise Note"""
        try:
            exercise_note= Exercise_Note.objects.filter(exercise_in_session=pk )
            serializer = ExerciseNoteSerializer(exercise_note, many=True)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Exercise_Note.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """handel GET requests for all Exercise Notes"""
        exercise_notes= Exercise_Note.objects.all()
        #filter for user and exercise in session id? and session? exerciseInSession.session.id?
        exercise_in_session = request.query_params.get('exercise_in_session', None)   
        # exercise = request.query_params.get('exercise', None)
        
        if exercise_in_session is not None:
            exercise_notes = exercise_notes.filter(exercise_in_session__id=exercise_in_session)
        
        # if exercise is not None:
        #     exercise_notes = exercise_notes.filter(exercise__id=exercise)
            
        serializer = ExerciseNoteSerializer(exercise_notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    def create(self, request):
        """Post Request for Exercise Note"""
        exercise_in_session = Exercise_In_Session.objects.get(pk=request.data['exercise_in_session'])
        serializer = CreateExerciseNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(exercise_in_session=exercise_in_session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

    
    #update note to include tags
    def update(self, request, pk): 
        exercise_note = Exercise_Note.objects.get(pk=pk)
        exercise_in_session = Exercise_In_Session.objects.get(pk=request.data["exercise_in_session"])
        exercise_note.description = request.data["description"]
        exercise_note.tags.add(*request.data["tags"])
        exercise_note.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

            
    @action(methods=['get'], detail=False)
    def getLastNote(self, request):
        exercise_notes= Exercise_Note.objects.all().last()
        serializer = ExerciseNoteSerializer(exercise_notes, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    