import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIRequestFactory

from .models import Participant
from .views import authenticate_digid


class ParticipantModelTests(TestCase):

    def test_participant_is_invalid(self):
        '''
        Participant does not exist in the system
        '''
        factory  = APIRequestFactory()
        request  = factory.post('http://127.0.0.1:8000/mockdigid/authenticate?username=TEST&password=TEST')
        response = authenticate_digid(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['msg'], 'Username or password is wrong')

    def test_participant_is_valid(self):
        '''
        Valid Participant, return details
        '''
        username = 'abc'
        user = User.objects.create_user(username=username, password=username,
                                        first_name='a', last_name='a')
        p = Participant.objects.create(user=user)

        factory  = APIRequestFactory()
        request  = factory.post('http://127.0.0.1:8000/mockdigid/authenticate?username={}&password={}'.format(username, username))
        response = authenticate_digid(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['first_name'], 'a')
        self.assertEqual(response.data['last_name'],  'a')
        self.assertEqual(response.data['bio'],  '')
