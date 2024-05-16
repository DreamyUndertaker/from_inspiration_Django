from django.contrib.auth.forms import UserChangeForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput, EmailField, CharField
from django import forms

from .models import Comment, UserProfile


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'id': 'comment-text',
                'label': '',
                'help-text': '',

            })
        }


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'id': 'comment-text',
                'label': '',
                'help-text': '',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'id': 'comment-text',
                'label': '',
                'help-text': '',
            })
        }


class ProfileUpdateForm(ModelForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Логин',
            'id': 'hello',
            'help_text': ''
        }
    ))
    email = EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Почта',
            'id': 'hello',
            'help_text': ''
        }
    ))
    first_name = CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Имя',
            'id': 'hello',
            'help_text': ''
        }
    ))
    last_name = CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Фамилия',
            'id': 'hello',
            'help_text': ''
        }
    ))
    picture = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={
            'class': 'form-control',
            'id': 'hello',
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'picture']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user.userprofile.picture = self.cleaned_data['picture']
            user.userprofile.save()
        return user


