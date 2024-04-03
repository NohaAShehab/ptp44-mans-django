

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'password1','password2', 'first_name', 'last_name', 'email')
