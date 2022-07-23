from django.urls import path

from account_engine import views

urlpatterns = [
    path("user-registration/", views.user_registration, name="user_registration"),
    path("user-login/", views.user_login, name="user_login"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("index", views.index, name="index"),
]
