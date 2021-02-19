from django.http.response import JsonResponse
from rest_framework import generics

from .models import TopUpEvent, PaymentEvent
from .serializers import TopUpEventSerializer, PaymentEventSerializer
from payments.models import PaymentMethod


class TopUp(generics.CreateAPIView):
    serializer_class = TopUpEventSerializer

    def post(self, request, *args, **kwargs):
        does_card_exist = PaymentMethod.objects.filter(card_number=request.POST.get('card_number')).exists()
        if does_card_exist:
            customer = PaymentMethod.objects.get(card_number=request.POST.get('card_number'))
            if int(request.POST.get('amount')) > 0:
                TopUpEvent.objects.create(
                    event_type=request.POST.get('event_type'),
                    card_number=request.POST.get('card_number'),
                    method=request.POST.get('method'),
                    amount=request.POST.get('amount'),
                    accepted=True
                )

                customer.balance += int(request.POST.get('amount'))
                customer.save()

                return JsonResponse({'status': 'accepted', 'reason': 'Card number does exist'})

            TopUpEvent.objects.create(
                event_type=request.POST.get('event_type'),
                card_number=request.POST.get('card_number'),
                method=request.POST.get('method'),
                amount=request.POST.get('amount'),
                accepted=False
            )

            return JsonResponse({'status': 'rejected', 'reason': 'Amount must be greater than 0'})

        return JsonResponse({'status': 'rejected', 'reason': 'Card number does not exist'})


class Payment(generics.CreateAPIView):
    serializer_class = PaymentEventSerializer

    def post(self, request, *args, **kwargs):
        does_card_exist = PaymentMethod.objects.filter(card_number=request.POST.get('card_number')).exists()
        if does_card_exist:
            customer = PaymentMethod.objects.get(card_number=request.POST.get('card_number'))
            if customer.balance >= int(request.POST.get('amount')):
                PaymentEvent.objects.create(
                    card_type=request.POST.get('card_type'),
                    card_number=request.POST.get('card_number'),
                    merchant_id=request.POST.get('merchant_id'),
                    merchant_name=request.POST.get('merchant_name'),
                    amount=request.POST.get('amount'),
                    accepted=True
                )

                customer.balance -= int(request.POST.get('amount'))
                customer.save()

                return JsonResponse({'status': 'accepted', 'reason': 'Funds are available'})

            PaymentEvent.objects.create(
                card_type=request.POST.get('card_type'),
                card_number=request.POST.get('card_number'),
                merchant_id=request.POST.get('merchant_id'),
                merchant_name=request.POST.get('merchant_name'),
                amount=request.POST.get('amount'),
                accepted=False
            )

            return JsonResponse({'status': 'rejected', 'reason': 'Insufficient funds available'})

        return JsonResponse({'status': 'rejected', 'reason': 'Card details do not exist'})


