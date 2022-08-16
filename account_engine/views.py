from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.core.mail import BadHeaderError, send_mail
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from account_engine.forms import ProfileEditForm, RegistrationForm, UserEditForm, SignUpForm
from account_engine.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate
from post_engine .models import Post
# Create your views here.




def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"HI! {username}.")
                    return redirect("index")
                else:
                    messages.error(request, "invalid username or password ")
            else:
                messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "account_engine/login.html", {"form": form})


def edit_profile(request):
    user_form = UserEditForm()
    profile_form = ProfileEditForm()
    if request.method == "POST":
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST,
        )
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Todo will write a alert message here in future
            return redirect(request, "account_engine/profile")
        else:
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "account_engine/edit_profile.html",
        {
            "edit_user_form": user_form,
            "edit_profile_form": profile_form,
        },
    )


def profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    user = profile.user
    posts = Post.objects.filter(user=user).order_by('-date')
    context = {'user':user,'posts':posts,'profile':profile,}

    return render(request, 'account_engine/profile.html',context)


    return render(request, "account_engine/profile.html")

#
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'account_engine/signup.html',{'form':form})


def user_registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(user=new_user)
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('user_login')
    else:
        form = SignUpForm()
    return render(request,'account_engine/signup.html', {'form':form})



def user_logout(request):
    logout(request)
    return redirect("user_login")


def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            login(request, request.user)
            messages.success(request, ("password successfully changed"))
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(
        request, "account_engine/password_reset/password_change.html", {"form": form}
    )
