from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('identifier', 'password', 'date_of_birth')
