from rest_framework import serializers
from django.contrib.auth.models import User
from swoleapi.models.swole_user import Swole_User

class UserSerializer(serializers.ModelSerializer):
    """JSON Serializer for Users"""
    class Meta:
        model = User   
        fields = ( "username", "first_name", "last_name", "email")
        
class SwoleUserSerializer(serializers.ModelSerializer):
    """JSON Serializer for Swole_Users"""
    user = UserSerializer()
    
    class Meta:
        model = Swole_User
        fields = ("id", "user", "profile_picture_url")
        
        