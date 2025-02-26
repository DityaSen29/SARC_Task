from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class AddMoneyForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class TransactionForm(forms.Form):
    recipient_id = forms.CharField(max_length=1)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
