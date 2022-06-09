"""View for handling Session requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.models.session import Session
from swoleapi.serializers.session_serializer import ExerciseInSessionSerializer, SessionSerializer

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
        #user = Swole_User.objects.get(user=reque)
        sessions = Session.objects.all()
        
        get_by_user = self.request.query_params.get('user_id', None)
        if get_by_user is not None:
            sessions = Session.objects.filter(user_id = get_by_user)
            
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

