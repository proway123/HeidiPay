from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import PaymentMethod
from .forms import PaymentCreate
from api.models import PaymentEvent


@login_required
def homepage(request):
    transactions = None
    payment = None

    if PaymentMethod.objects.filter(user=request.user).exists():
        payment = PaymentMethod.objects.get(user=request.user)
        transactions = PaymentEvent.objects.filter(card_number=payment.card_number)

    form = PaymentCreate(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            payment_method = form.save(commit=False)
            payment_method.user = request.user
            payment_method.save()

    context = {
        'form': form,
        'payment_method': payment,
        'transactions': transactions
    }

    return render(request, 'home.html', context)
