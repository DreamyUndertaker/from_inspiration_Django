from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput

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
    class Meta:
        model = UserProfile
        fields = ['picture']
