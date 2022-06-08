"""View for handling Exercise requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from swoleapi.models import Exercise
from swoleapi.serializers.exercise_serializer import ExerciseSerializer

class ExerciseView(ViewSet):
    """Swole Session View"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single exercise
        Returns:
            Response--JSON serialized exercise
        """
        try:
            exercise = Exercise.objects.get(pk=pk)
            serializer = ExerciseSerializer(exercise)
            return Response (serializer.data)
        except Exercise.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handel Get Requests to get all exercises"""
        
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    
    #Stretch goal functionality ..........
    # def create(self, request):
    #     """Handle POST operations"""
        
        