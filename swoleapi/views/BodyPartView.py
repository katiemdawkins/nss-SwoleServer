"""View for handling Body Part requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from swoleapi.models import body_part
from swoleapi.models.body_part import Body_Part
from swoleapi.serializers.body_part_serializer import BodyPartSerializer

class BodyPartView(ViewSet):
    """Body Part View"""
    
    #Get Single Body Part for Exercise Lists
    
    def retrieve(self, request, pk):
        """Handle GET Requests for Single Body_Part"""
        try:
            body_part = Body_Part.objects.get(pk=pk)
            serializer = BodyPartSerializer(body_part)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Body_Part.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    #Get All Body Parts for Exercise Lists
    
    def list(self, request):
        """Handle GET requests for all Body Parts"""
        body_parts = Body_Part.objects.all()
        serializer = BodyPartSerializer(body_parts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)