from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class VerificationForm(forms.Form):
    verify_code = forms.CharField(max_length=12, label='Введите код верификации')
