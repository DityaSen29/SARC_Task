from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, BudgetForm, TransactionForm
from .models import Budget, Transaction

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'tracker/register.html', {'form': form})

@login_required
def dashboard(request):
    budget = Budget.objects.filter(user=request.user).first()
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'tracker/dashboard.html', {'budget': budget, 'transactions': transactions})

@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('dashboard')
    else:
        form = BudgetForm()
    return render(request, 'tracker/add_budget.html', {'form': form})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        reason = request.POST.get('reason')
        amount = request.POST.get('amount')

        if date and reason and amount:
            transaction = Transaction(user=request.user, date=date, reason=reason, amount=amount)
            transaction.save()
            return redirect('dashboard')

    return render(request, 'tracker/add_transaction.html')
