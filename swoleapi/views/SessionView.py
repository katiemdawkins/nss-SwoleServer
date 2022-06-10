"""View for handling Session requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.models.session import Session
from swoleapi.models.exercise import Exercise
from swoleapi.models.swole_user import Swole_User
from rest_framework.decorators import action
from swoleapi.serializers.session_serializer import CreateSessionSerializer, UpdateSessionSerializer, ExerciseInSessionSerializer, SessionSerializer
from swoleapi.serializers.exercise_in_session_serializer import CreateExerciseInSession

class TrainingLogView(ViewSet):
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

    def list(self, request):
        """Handle GET Requests to get all sessions"""
        
        sessions = Session.objects.all().order_by("-date")
        swole_user = Swole_User.objects.get(user=request.auth.user)
            
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST Requests for New Sessions"""
        user = Swole_User.objects.get(pk=request.auth.user.id)
        
        serializer = CreateSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    #custom action that changes false to true on is_completed
    @action(methods=['Put'],detail=True)
    def isCompleteTrue(self, request, pk):
        """"Put Request """

        session = Session.objects.get(pk=pk, user=request.auth.user.id)
        session.date = request.data['date']
        session.rating = request.data['rating']
        session.is_complete = True
        serializer = UpdateSessionSerializer(session, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        
        






















