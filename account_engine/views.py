from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


from account_engine.forms import (ProfileEditForm, RegistrationForm,
                                  UserEditForm)
from account_engine.models import Profile

# Create your views here.


def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(user=new_user)
            messages.success(request, "Account Created")
            return redirect("user_login")
    else:
        form = RegistrationForm()
    return render(request, "account_engine/registration.html", {"form": form})


def user_login(request):
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


def profile(request):

    return render(request,'account_engine/profile.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')


