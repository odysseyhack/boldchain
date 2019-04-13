from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from giftcards.models import PensionEntity


class Command(BaseCommand):
    help = 'Create test PensionEntity'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of PensionEntities to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        for i in range(total):
            kwargs = {
                'username': 'PE{}'.format(i),
                'password': 'test',
                'first_name': 'PE_{}'.format(i),
                'email': 'test{}@entity.com'.format(i)
            }

            user = User.objects.create_user(**kwargs)
            PensionEntity.objects.create(user=user)
