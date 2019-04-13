import datetime

from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIRequestFactory

from .models import Giftcard
from .views import giftcard_valid


class GiftcardModelTests(TestCase):

    def test_giftcard_is_invalid(self):
        '''
        Gift card is not valid
        '''
        factory  = APIRequestFactory()
        request  = factory.get('http://127.0.0.1:8000/giftcards/valid?barcode=INVALIDBARCODE')
        response = giftcard_valid(request)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['msg'], 'Invalid barcode')

    def test_giftcard_is_valid(self):
        '''
        Valid giftcard, return amount
        '''
        barcode = 'abc'
        amount  = 10.0
        Giftcard.objects.create(barcode=barcode, amount=amount)

        factory  = APIRequestFactory()
        request  = factory.get('http://127.0.0.1:8000/giftcards/valid?barcode={}'.format(barcode))
        response = giftcard_valid(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['barcode'], barcode)
        self.assertEqual(response.data['amount'],  amount)
