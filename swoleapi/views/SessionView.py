"""View for handling Session requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.models.session import Session
from swoleapi.serializers.session_serializer import ExerciseInSessionSerializer, SessionSerializer

class SessionView(ViewSet):
    """Swole Session View"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single session
        Returns:
            Response--JSON serialized session
        """
        try:
            #get all exercises in session 
            exercisesInSession = Exercise_In_Session.objects.filter(session = pk)
            exercisesInSession = ExerciseInSessionSerializer(exercisesInSession, many= True)
            
            #get session
            session = Session.objects.get(pk=pk)
            serializer = SessionSerializer(session)
            return Response (serializer.data)
        except Session.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


        
