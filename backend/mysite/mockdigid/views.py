from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Participant


@api_view(['POST'])
def connect_digid(request):
    '''
    Check if login credentials are right
    '''
    return Response({'valid':'asdfasf'}, status=status.HTTP_200_OK)
