from django.contrib import admin
from .models import TopUpEvent, PaymentEvent


admin.site.register(TopUpEvent)
admin.site.register(PaymentEvent)
