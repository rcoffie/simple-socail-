from django import forms
from post_engine.models import PostInfo


class PostInfoForm(forms.ModelForm):
    class Meta:
        model = PostInfo
        fields = ['post', 'image']