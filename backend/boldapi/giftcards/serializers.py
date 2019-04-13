from rest_framework import serializers
from .models import Giftcard


class GiftcardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Giftcard
        fields = ("barcode", "amount")
