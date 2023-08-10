from .models import Post, Comment
from django import forms


class Form(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('slug', 'created_on', 'status', 'updated_on',)


class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_title', 'comment_content')