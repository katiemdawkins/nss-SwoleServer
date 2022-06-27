"""View for handling Category requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from swoleapi.models.category import Category
from swoleapi.serializers.category_serializer import CategorySerializer

class CategoryView(ViewSet):
    """Category View"""
    
    #Get Single Category for Exercise List
    def retrieve(self, request, pk):
        """Handle GET Requests for Single Category"""
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    #Get All Categories for Exercise List
    def list(self, request):
        """Handle GET requests for all Categories"""
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)