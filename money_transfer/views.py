from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Transfer, Savings
import requests
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Transfer, Savings
import requests
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from itertools import chain

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {
        'transfers': get_user_transfers(request.user),
        # 'savings': get_user_savings(request.user)
    }
    return render(request, 'home.html', context)

def get_user_transfers(user):
    # Safe access to sent and received transfers using related_name
    sent_transfers = user.sent_transfers.all() if hasattr(user, 'sent_transfers') else []
    received_transfers = user.received_transfers.all() if hasattr(user, 'received_transfers') else []
    return list(chain(sent_transfers, received_transfers))

def get_user_savings(user):
    return user.savings.all()


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def transfer_money(request):
    if request.method == 'POST':
        sender = request.user
        recipient_phone = request.POST['recipient_phone']
        recipient = get_object_or_404(User, mobile_number=recipient_phone)
        amount = request.POST['amount']

        exchange_rate = _get_exchange_rate(sender.mobile_money_provider, recipient.mobile_money_provider)
        fee = _calculate_fee(float(amount))
        recipient_amount = float(amount) - fee

        transfer = Transfer.objects.create(
            sender=sender, recipient=recipient, amount=amount, fee=fee, exchange_rate=exchange_rate
        )

        sender.balance -= float(amount)
        recipient.balance += recipient_amount
        sender.save()
        recipient.save()

        _send_sms_notification(transfer)

        messages.success(request, 'Transfer completed successfully')
        return redirect('home')

    return render(request, 'transfer.html')
def send_money(request):
    return render(request, 'send_money.html')

def pay_utilities(request):
    return render(request, 'pay_utilities.html')

def book_ticket(request):
    return render(request, 'book_ticket.html')

def book_cinema(request):
    return render(request, 'book_cinema.html')

def pay_bus_fare(request):
    return render(request, 'pay_bus_fare.html')

def savings(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        recurring = 'recurring' in request.POST
        savings = Savings.objects.create(user=request.user, amount=amount, recurring=recurring)

        _send_sms_notification(savings)

        messages.success(request, 'Savings created successfully')
        return redirect('home')

    return render(request, 'savings.html')

def _get_exchange_rate(sender_provider, recipient_provider):
    url = f"https://api.example.com/exchange-rate?from={sender_provider}&to={recipient_provider}"
    response = requests.get(url)
    return response.json()['rate']

def _calculate_fee(amount):
    return amount * 0.01  # 1% fee

def _send_sms_notification(obj):
    if isinstance(obj, Transfer):
        message = f"Transfer of {obj.amount} from {obj.sender.mobile_number} to {obj.recipient.mobile_number} completed."
    elif isinstance(obj, Savings):
        message = f"You've just saved {obj.amount} towards your goal."
