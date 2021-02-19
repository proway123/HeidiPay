from django.db import models
from users.models import CustomUser


class PaymentMethod(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    card_number = models.IntegerField(unique=True, max_length=16)
    balance = models.IntegerField(unique=False, max_length=16, default=0)

    def __str__(self):
        return "Card number {}".format(self.card_number)
