from django import forms

from .models import PaymentMethod


class PaymentCreate(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ('card_number',)
