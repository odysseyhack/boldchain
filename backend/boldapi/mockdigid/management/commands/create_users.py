from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from mockdigid.models import Participant


class Command(BaseCommand):
    help = 'Create test users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        for i in range(total):
            kwargs = {
                'username': 'test{}'.format(i),
                'password': 'test',
                'first_name': 'first{}'.format(i),
                'last_name': 'last{}'.format(i),
                'email': 'test{}@admin.com'.format(i)
            }

            user = User.objects.create_user(**kwargs)
            Participant.objects.create(user=user)
