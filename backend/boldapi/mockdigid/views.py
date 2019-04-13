from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Participant


@api_view(['POST'])
def authenticate_digid(request):
    '''
    Check if user is valid (Will be replaced with BasicAuth in the future)

    Example call: 127.0.0.1:8000/mockdigid/authenticate?username=TEST&password=TEST
    '''
    user = authenticate(username=request.query_params['username'],
                        password=request.query_params['password'])

    try:
        participant = Participant.objects.get(user=user)
    except Participant.DoesNotExist:
        return Response({'msg': 'Username or password is wrong'}, status=status.HTTP_200_OK)

    return_dict = {
        'first_name': participant.user.first_name,
        'last_name' : participant.user.last_name,
        'bio'       : participant.bio
    }

    return Response(return_dict, status=status.HTTP_200_OK)
