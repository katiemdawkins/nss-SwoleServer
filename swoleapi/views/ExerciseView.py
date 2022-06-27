"""View for handling Exercise requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from swoleapi.models import Exercise
from swoleapi.serializers.exercise_serializer import ExerciseSerializer

class ExerciseView(ViewSet):
    """Swole Exercise View"""
    
    #get a single exercise by id for exercise details page
    def retrieve(self, request, pk):
        """Handle GET requests for single exercise
        Returns:
            Response--JSON serialized exercise
        """
        try:
            exercise = Exercise.objects.get(pk=pk)
            serializer = ExerciseSerializer(exercise)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Exercise.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    #filter the exercise list by name, category, and body part for Exercise Page and Add Exercise to Session Page
    #order list by name
    def list(self, request):
        """Handel Get Requests to get all exercises"""
        
        exercises = Exercise.objects.all().order_by("name")
        
        name = request.query_params.get('name', None)
        category = request.query_params.get('category', None)
        body_part = request.query_params.get('body_part', None)
        
        if name is not None:
            exercises = exercises.filter(name__icontains=name)
        
        if category is not None:
            exercises = exercises.filter(category__id=category)
            
        if body_part is not None:
            exercises = exercises.filter(body_part__id=body_part)
                
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #Stretch goal functionality ..........
    # def create(self, request):
    #     """Handle POST operations"""
        
        