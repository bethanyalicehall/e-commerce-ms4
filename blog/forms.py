from .models import Post, Comment
from django import forms


class Form(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('slug', 'created_on', 'status', 'updated_on',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
