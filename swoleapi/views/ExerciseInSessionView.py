from logging import raiseExceptions
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from swoleapi.models.session import Session
from swoleapi.models.exercise import Exercise
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.serializers.exercise_in_session_serializer import CreateExerciseInSession
from swoleapi.serializers.session_serializer import ExerciseInSessionSerializer, UpdateExerciseInSessionSerializer


class ExerciseInSessionView(ViewSet):
    
    def retrieve(self, request, pk):
        try:
            exercise_in_session = Exercise_In_Session.objects.get(pk=pk)
            serializer = ExerciseInSessionSerializer(exercise_in_session)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Exercise_In_Session.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    #for user viewing workout in progress
    def list(self, request):
        """Handle GET requests for Exercises In Session"""
        
        exercises_in_session = Exercise_In_Session.objects.all()
        session = request.query_params.get('session', None)
        if session is not None:
            exercises_in_session = exercises_in_session.filter(session__id = session).order_by("date", "exercise__id")
        
        serializer = ExerciseInSessionSerializer(exercises_in_session, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #when user adds a set to an exercise
    def create(self, request):
        """Post Request for Exercise In Session"""
        exercise = Exercise.objects.get(pk=request.data['exercise'])
        session = Session.objects.get(pk=request.data['session'])
        serializer = CreateExerciseInSession(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(exercise=exercise, session=session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    #when User Edits details of set, rep, load
    def update(self, request, pk):
        """Handle PUT requests for Exercise In Session"""
        
        exercise_in_session = Exercise_In_Session.objects.get(pk=pk)
        serializer = UpdateExerciseInSessionSerializer(exercise_in_session, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (None, status=status.HTTP_204_NO_CONTENT)