from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post',)
        labels = {
            'name': 'お名前',
            'text': 'コメント'
        }