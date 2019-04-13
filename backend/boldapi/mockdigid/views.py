import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Participant, PensionFund


def _get_participant_pension_funds(participant):
    '''
    Return list of all pension funds of a participant
    '''
    response = []
    pensions = list(PensionFund.objects.filter(participant=participant))

    print(pensions)

    for pension in pensions:
        response.append({
            'fund_name': pension.fund_name,
            'bsn': pension.bsn,
            'active': pension.active,
            'start_date': pension.start_date,
            'ascription': pension.ascription,
            'eligible': pension.eligible,
            'fulltime_salary': pension.fulltime_salary,
            'entitlements': pension.entitlements
        })

    return response

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
        'first_name'   : participant.user.first_name,
        'last_name'    : participant.user.last_name,
        'bio'          : participant.bio,
        'pension_funds': _get_participant_pension_funds(participant)
    }

    return Response(return_dict, status=status.HTTP_200_OK)
