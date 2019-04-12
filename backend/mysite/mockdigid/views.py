from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate

from .models import Participant


@api_view(['POST'])
def authenticate_digid(request):
    '''
    Check if user is valid
    '''

    print(request.data)

    participant = authenticate(username=request.POST['username'], password=request.POST['password'])

    if participant is not None:
        print("Hola")
    else:
        return Response({'msg': 'Invalid User'}, status=status.HTTP_200_OK)

    return Response({'msg': 'Hola'}, status=status.HTTP_200_OK)
