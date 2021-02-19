from django.db import models


class TopUpEvent(models.Model):
    event_type = models.CharField(max_length=40, default='')
    card_number = models.IntegerField(unique=False, max_length=16, default=0)
    method = models.CharField(max_length=40, default='')
    amount = models.IntegerField(unique=False, max_length=16, default=0)
    accepted = models.NullBooleanField(default=None)

    def __str__(self):
        return "Top up: card {}, amount {}".format(self.card_number, self.amount)


class PaymentEvent(models.Model):
    card_type = models.CharField(max_length=40)
    card_number = models.IntegerField(unique=False, max_length=16)
    merchant_id = models.IntegerField(unique=False, max_length=4)
    merchant_name = models.CharField(max_length=50)
    amount = models.IntegerField(unique=False, max_length=16, default=0)
    accepted = models.NullBooleanField(default=None)

    def __str__(self):
        return "Payment: to {}, amount {}".format(self.merchant_name, self.amount)
