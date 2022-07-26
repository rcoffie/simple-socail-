from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from account_engine.forms import (ProfileEditForm, RegistrationForm,
                                  UserEditForm)
from account_engine.models import Profile
from django.contrib import messages
# Create your views here.


def user_registration(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
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
    if request.user.is_authenticated:
        return redirect('profile')
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


def profile(request):

    return render(request,'account_engine/profile.html')

def index(request):
    return render(request, "index.html")


def user_logout(request):
    logout(request)
    return redirect('user_login')



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')

					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    #Todo change the redirect view in future
					return redirect ("profile")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})
