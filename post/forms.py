from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Comment
        exclude = ('post',)
        labels = {
            'name': 'Your Name',
            'text': 'Your Comment'
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }
