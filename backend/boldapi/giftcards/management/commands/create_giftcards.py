import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.crypto import get_random_string

from giftcards.models import Giftcard, PensionEntity


class Command(BaseCommand):
    help = 'Create test giftcards'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        for i in range(total):
            kwargs = {
                'barcode': get_random_string(length=10),
                'issued_by': PensionEntity.objects.order_by('?')[0],
                'amount': random.randint(10, 50),
                'created': timezone.now()
            }

            Giftcard.objects.create(**kwargs)
