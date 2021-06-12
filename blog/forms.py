from django import forms
from .models import Post, Comment

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'author')
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'current_user', 'type': 'hidden'}),
        }
        labels = {
            'comment': ('Treść komentarza'),
        }