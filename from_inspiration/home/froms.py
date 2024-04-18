from django.forms import ModelForm, Textarea, TextInput

from home.models import Comment


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
