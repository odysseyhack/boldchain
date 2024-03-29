from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Giftcard
from .serializers import GiftcardsSerializer


@api_view(['GET'])
def giftcard_valid(request):
    '''
    Check if gift card is valid

    Example call: http://127.0.0.1:8000/giftcards/valid?barcode=INVALIDBARCODE
    '''
    try:
        giftcard = Giftcard.objects.get(barcode=request.query_params['barcode'])
    except Giftcard.DoesNotExist:
        return Response({'msg': 'Invalid barcode'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'barcode': giftcard.barcode, 'amount': giftcard.amount}, status=status.HTTP_200_OK)
