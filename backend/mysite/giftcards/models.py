import uuid

from django.contrib.auth.models import User
from django.db import models


class Giftcard(models.Model):
    '''
    Model describes the Giftcard
    '''
    barcode   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner     = models.ForeignKey('Profile', on_delete=models.CASCADE)

    redeemed  = models.BooleanField('Is the card redeemed?')
    created   = models.DateTimeField('Date of creation')
    activated = models.DateTimeField('Activated on')
    validity  = models.DateTimeField('Valid until')


class Profile(models.Model):
    '''
    Profile can be any of {'Super', 'PensionEntity', 'Participant'}

    'Super'        : is the superuser. For development purposes
    'PensionEntity': can be something like "APG"
    'Participant'  : is the customer. They can link their Digid to the system, view
                     projections, etc.
    '''
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    email        = models.EmailField(max_length=100)
    image        = models.ImageField()   # TODO
    profile_type = models.CharField(max_length=30, default='Participant')
    bio          = models.TextField(max_length=500, blank=True)
    location     = models.CharField(max_length=30, blank=True)
    birth_date   = models.DateField(null=True, blank=True)
