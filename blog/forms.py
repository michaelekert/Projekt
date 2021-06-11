from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'row':10}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'current_user', 'type': 'hidden'}),
        }
        labels = {
            'title': ('Tytuł posta'),
            'text': ('Treść posta'),
        }