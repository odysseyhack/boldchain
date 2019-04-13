import json

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


class PensionFund(models.Model):
    '''
    Details of the pension fund
    '''
    bsn        = models.CharField(max_length=100, primary_key=True)
    fund_name  = models.CharField(max_length=100)
    active     = models.BooleanField(default=False)

    ascription = models.CharField(max_length=100, null=True)
    eligible   = models.BooleanField(default=True)
    start_date = models.DateField(null=True, blank=True)
    end_date   = models.DateField(null=True, blank=True)

    fulltime_salary = models.FloatField(default=0.0)
    entitlements    = models.CharField(max_length=1000)

    def set_entitlements(self, x):
        self.entitlements = json.dumps(x)

    def get_entitlements(self, x):
        return json.loads(self.entitlements)
