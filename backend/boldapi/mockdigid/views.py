import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mockdigid.models import Participant, PensionFund
from giftcards.models import Giftcard


def _get_participant_pension_funds(participant):
    '''
    Return list of all pension funds of a participant
    '''
    response = []
    pensions = list(PensionFund.objects.filter(participant=participant))

    for pension in pensions:
        response.append({
            'fund_name': pension.fund_name,
            'id': pension.session_id,
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
        return Response({'msg': 'Username or password is wrong'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({
            'first_name'   : participant.user.first_name,
            'last_name'    : participant.user.last_name,
            'bio'          : participant.bio,
            'pension_funds': _get_participant_pension_funds(participant)
        }, status=status.HTTP_200_OK)


@api_view(['PUT'])
def add_to_fund(request):
    '''
    Add giftcard amount to a fund
    '''
    try:
        giftcard = Giftcard.objects.get(barcode=request.query_params['barcode'])
        pension_fund = PensionFund.objects.get(session_id=request.query_params['id'])
    except Giftcard.DoesNotExist:
        return Response({'msg': 'Invalid barcode'}, status=status.HTTP_400_BAD_REQUEST)
    except PensionFund.DoesNotExist:
        return Response({'msg': 'Invalid Pension Fund'}, status=status.HTTP_400_BAD_REQUEST)

    pension_fund.amount += giftcard.amount
    pension_fund.save()

    return Response({
            'amount': pension_fund.amount,
            'msg': 'Amount added to pension fund',
            'link': pension_fund.get_web_link()
        }, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_participant(request):
    '''
    Create a new user
    '''
    try:
        user = User.objects.create_user(username=request.query_params['username'],
                                        password=request.query_params['password'])
        Participant.objects.create(user=user)
    except:
        return Response({'msg': 'Unable to create user'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'msg': 'Created new user'}, status=status.HTTP_200_OK)
