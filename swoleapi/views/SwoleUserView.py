"""View for handling Swole User Requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from swoleapi.models.swole_user import Swole_User
from swoleapi.serializers.user_serializer import SwoleUserSerializer

class SwoleUserView(ViewSet):

    def retrieve(self,request, pk):
        try:
            swole_user=Swole_User.objects.get(user=request.auth.user)
            serializer = SwoleUserSerializer(swole_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Swole_User.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        swole_users=Swole_User.objects.all()
        serializer = SwoleUserSerializer(swole_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        