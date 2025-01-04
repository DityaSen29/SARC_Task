from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Transaction
from .forms import RegisterForm, LoginForm, AddMoneyForm, TransactionForm
from django.contrib import messages

def home(request):
    if 'user_id' in request.session:
        return redirect('dashboard') 
    return render(request, 'tracker/home.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_id = str(User.objects.count() % 9 + 1)
            user.save()
            messages.success(request, f"Registered successfully! Your ID: {user.user_id}")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'tracker/register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials!")
    else:
        form = LoginForm()
    return render(request, 'tracker/login.html', {'form': form})

def dashboard(request):
    user = get_object_or_404(User, id=request.session.get('user_id'))
    return render(request, 'tracker/dashboard.html', {'user': user})

def add_money(request):
    user = get_object_or_404(User, id=request.session.get('user_id'))
    if request.method == "POST":
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            user.balance += form.cleaned_data['amount']
            user.save()
            messages.success(request, "Money added successfully!")
            return redirect('dashboard')
    else:
        form = AddMoneyForm()
    return render(request, 'tracker/add_money.html', {'form': form})

def make_transaction(request):
    user = get_object_or_404(User, id=request.session.get('user_id'))
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            recipient_id = form.cleaned_data['recipient_id']
            amount = form.cleaned_data['amount']
            recipient = User.objects.filter(user_id=recipient_id).first()
            if recipient and user.balance >= amount:
                user.balance -= amount
                recipient.balance += amount
                user.save()
                recipient.save()
                Transaction.objects.create(sender=user, recipient=recipient, amount=amount)
                messages.success(request, "Transaction successful!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid transaction!")
    else:
        form = TransactionForm()
    return render(request, 'tracker/make_transaction.html', {'form': form})
