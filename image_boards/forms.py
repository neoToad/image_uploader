from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']
        labels = {'text': 'Add a post:'}
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Title'}),
        }