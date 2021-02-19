from rest_framework import serializers
from .models import TopUpEvent, PaymentEvent


class TopUpEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopUpEvent
        fields = ('event_type', 'card_number', 'method', 'amount')


class PaymentEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentEvent
        fields = ('card_type', 'card_number', 'merchant_id', 'merchant_name', 'amount')
