from django import forms
from .models import CustomUser


class SignupForm(forms.Form):
    login = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username or Email',
            'label': 'Username or Email',
            'id': 'login'
        })
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'label': 'Password',
            'id': 'password'
        })
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y', attrs={
            'class': 'form-control',
            'placeholder': 'Date of Birth',
            'label': 'Date of Birth',
            'id': 'date_of_birth'
        })
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if CustomUser.objects.filter(login=login).exists():
            raise forms.ValidationError('This username or email is already in use.')
        return login

    def save(self):
        pass


class SigninForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
        })
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        })
    )