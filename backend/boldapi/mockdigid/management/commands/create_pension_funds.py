import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from mockdigid.models import Participant, PensionFund


class Command(BaseCommand):
    help = 'Create test pension funds'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        for i in range(total):
            kwargs = {
                'session_id': 'sess_id_{}'.format(get_random_string(length=5)),
                'bsn': 'BSN_{}'.format(i),
                'participant': Participant.objects.order_by('?')[0],
                'fund_name': random.choice(['abp', 'pfzw', 'sf', 'gf']),
                'active': random.choice([True, False]),
                'ascription': random.choice(['ABP', 'PFZW', 'Some Fund', 'Gold Fund']),
                'fulltime_salary': random.randint(100, 200)
            }

            PensionFund.objects.create(**kwargs)
