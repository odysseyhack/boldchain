import uuid

from django.contrib.auth.models import User
from django.db import models


class Giftcard(models.Model):
    '''
    Model describes the Giftcard
    '''
    barcode   = models.CharField(max_length=100, primary_key=True)
    issued_by = models.ForeignKey('PensionEntity', on_delete=models.CASCADE, null=True)
    amount    = models.FloatField(default=0.0)
    created   = models.DateTimeField('Date of creation', null=True)
    validity  = models.DateTimeField('Valid until', null=True)

    def __str__(self):
        return "{} - {}".format(self.barcode, self.amount)


class Participant(models.Model):
    '''
    Participant is the customer. They can link their Digid to the system, view
    projections, etc.
    '''
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    bio        = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_username()


class PensionEntity(models.Model):
    '''
    PensionEntity can be something like "APG"
    '''
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    bio   = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_username()
