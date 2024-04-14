from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignupForm(forms.ModelForm):
    required_css_class = "form-control form-control-sm"

    class Meta:
        model = CustomUser
        fields = ('login', 'password', 'date_of_birth')
        widgets = {
            'login': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username or Email',
                'label': 'Username or Email',
                'id': 'login'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'label': 'Password',
                'id': 'password'
            }),
            'date_of_birth': forms.DateInput(format='%m/%d/%Y', attrs={
                'class': 'form-control',
                'placeholder': 'Date of Birth',
                'label': 'Date of Birth',
                'id': 'date_of_birth'
            }),

        }

