from django import forms
from post_engine.models import Post


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Post
        fields = ['post', 'image']
