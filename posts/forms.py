from django import forms
from .models import Post
from martor.fields import MartorFormField

class PostForm(forms.ModelForm):
    content = MartorFormField()
    class Meta:
        model = Post
        fields = [
            "title",
            "summary",
            "content",
            "image",
        ]