from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Логин',
            'id': 'hello',
            'help_text': ''
        }
    ))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Пароль',
            'id': 'hi',
            'help_text': '',
            'form_text': '',
            'label': 'Пароль',
            'title': ''
        }
    ))
    password1 = forms.CharField(required=False, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Пароль',
            'id': 'hi',
            'help_text': '',
            'form_text': '',
            'label': 'Пароль',
            'title': ''
        }
    ))
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль',
            'id': 'confirm_password',
            'help_text': '',
            'form_text': '',
            'label': 'Подтвердите пароль',
            'title': ''
        }
    ))
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Дата рождения',
            'id': 'date_of_birth',
        }
    ), input_formats=['%d/%m/%Y'])  # Ожидаемый формат даты

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth is None:
            raise ValidationError("Введите правильную дату.")
        return date_of_birth


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Temp',
            'id': 'hello'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Temp',
            'id': 'hi',
            'help_text': '',
        }
    ))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
