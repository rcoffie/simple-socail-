from django import forms
from social_app.models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("detail", "image")