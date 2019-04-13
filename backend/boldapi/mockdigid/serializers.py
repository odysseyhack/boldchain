from rest_framework import serializers
from .models import Participant


class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ("user")
