from rest_framework import serializers
from .models import Participant, PensionFund


class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ("user")

class PensionFundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PensionFund
        fields = ("fund_name", "active", "start_date", "end_date")
