from django import forms
from .models import Post, Response
from django.core.exceptions import ValidationError
import os


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'text',
            'image',
            'video',
            'document',
        ]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'text'
        ]