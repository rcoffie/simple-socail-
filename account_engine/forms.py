from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from account_engine.models import Profile


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional. ")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    email = forms.EmailField(
        max_length=254, help_text="Required. Inform a valid email address "
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "location", "birth_date")
