from logging import raiseExceptions
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from swoleapi.models.tag import Tag
from swoleapi.models.exercise_note import Exercise_Note
from swoleapi.serializers.tag_serializer import TagSerializer, CreateTagSerializer


class TagView(ViewSet):
    
    def retrieve(self, request, pk):
        try:
            tag= Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    
    def list(self, request):
        tags = Tag.objects.all().order_by('label')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

            
        
        