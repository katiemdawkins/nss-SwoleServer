"""View for handling Session requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from swoleapi.models.exercise_in_session import Exercise_In_Session
from swoleapi.models.session import Session
from swoleapi.models.exercise import Exercise
from swoleapi.models.swole_user import Swole_User
from swoleapi.serializers.session_serializer import CreateSessionSerializer, ShortSessionSerializer, TrainingLogSessionSerializer
from swoleapi.serializers.session_serializer import UpdateSessionSerializer
from rest_framework.decorators import action
from swoleapi.serializers.session_serializer import  ExerciseInSessionSerializer, SessionSerializer


class TrainingLogView(ViewSet):
    """Swole Session View"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single session
        Returns:
            Response--JSON serialized session
        """
        try:
            session = Session.objects.get(pk=pk)

            serializer = SessionSerializer(session)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Session.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    #when user is on Training Log and wants to view all their sessions
    def list(self, request):
        """Handle GET Requests to get all sessions"""
        
        sessions = Session.objects.all().order_by("-id")
        user = request.query_params.get("user", None)
        is_complete = request.query_params.get("is_complete", None)
        
        if user is not None:
            sessions = sessions.filter(user__id=user)
            
        if is_complete is not None:
            sessions = sessions.filter(is_complete=True)
                
        serializer = TrainingLogSessionSerializer(sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #when user clicks start session
    def create(self, request):
        """Handle POST Requests for New Sessions"""
        user = Swole_User.objects.get(pk=request.auth.user.id)
        
        serializer = CreateSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    #user can delete a session in the Training log 
    def destroy(self, request, pk):
        session = Session.objects.get(pk=pk)
        session.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    #when user clicks Finish Session - this custom action changes false to true on is_complete
    @action(methods=['Put'],detail=True)
    def isCompleteTrue(self, request, pk):
        """"Put Request to complete a session"""

        session = Session.objects.get(pk=pk, user=request.auth.user.id)
        session.date = request.data['date']
        session.rating = request.data['rating']
        session.is_complete = True
        serializer = UpdateSessionSerializer(session, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)   
        
    #when user adds a rating to a session before finishing
    def update(self, request, pk):
        """Handles Put Requests for Session"""
        
        session = Session.objects.get(pk=pk)
        serializer = UpdateSessionSerializer(session, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (None, status=status.HTTP_204_NO_CONTENT)
    
    
    #custom action to get completed sessions for a user
    #and calculate their average rating
    #ShortSession serializer to get less data back
    @action(methods=['GET'], detail =False)
    def getSessionsForRatings(self, request):
        
        sessions = Session.objects.all()
        user = request.query_params.get("user", None)
        is_complete = request.query_params.get("is_complete", None)
        
        if user is not None:
            sessions = sessions.filter(user__id=user)
        if is_complete is not None:
            sessions = sessions.filter(is_complete=True)
        
        ratings = []
        for session in sessions:
            ratings.append(session.rating)
            
        total_rating = 0
        for rating in ratings: 
            total_rating += rating   
                
        ave_rating =0
        if len(ratings) !=0:
            ave_rating = total_rating/ len(ratings)

        for session in sessions:
            session.averageRating = round(ave_rating)

        serializer = ShortSessionSerializer(sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




















