from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Giftcard
from .serializers import GiftcardsSerializer

# @api_view(['GET', 'POST'])
# def giftcard_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def giftcard_valid(request):
    '''
    Check if gift card is valid
    '''
    try:
        giftcard = Giftcard.objects.get(barcode=request.GET['barcode'])
    except Giftcard.DoesNotExist:
        return Response('Invalid barcode', status=status.HTTP_400_BAD_REQUEST)

    return Response({'barcode': giftcard.barcode, 'amount': giftcard.amount}, status=status.HTTP_200_OK)
