from django import forms
from post_engine.models import PostInfo


class PostInfoForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = PostInfo
        fields = ['post', 'image']
