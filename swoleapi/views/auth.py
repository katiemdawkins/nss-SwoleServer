from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from swoleapi.models.swole_user import Swole_User


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        
        data = {
            'valid': True,
            'token': token.key
        }
    else:
        data = { 'valid': False }
    return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
    request -- The full HTTP request object
    '''

    
    new_user = User.objects.create_user(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=request.data['email'],
        username=request.data['username'],
        password=request.data['password'],
    )

    
    swole_user = Swole_User.objects.create(
        user= new_user,
        profile_picture_url=request.data['profile_picture_url']
    )
    
    token = Token.objects.create(user=swole_user.user)
    
    
    data = { 'token': token.key }
    return Response(data, status=status.HTTP_201_CREATED)