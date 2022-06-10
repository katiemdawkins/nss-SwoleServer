from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from swoleapi.models.session import Session
from swoleapi.models.exercise import Exercise
from swoleapi.serializers.exercise_in_session_serializer import CreateExerciseInSession


class ExerciseInSessionView(ViewSet):
    def create(self, request):
        """Post Request for Exercise In Session"""
        exercise = Exercise.objects.get(pk=request.data['exercise'])
        session = Session.objects.get(pk=request.data['session'])
        serializer = CreateExerciseInSession(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(exercise=exercise, session=session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)