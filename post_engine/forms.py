from django import forms

from post_engine.models import Comment, Post


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ["post", "image"]


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label="Coment", widget=forms.TextInput(attrs={"placeholder": "Comment"})
    )

    class Meta:
        model = Comment
        fields = ["body"]
