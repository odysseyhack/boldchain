import uuid

from django.contrib.auth.models import User
from django.db import models


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
