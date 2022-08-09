from django.urls import path

from account_engine import views

urlpatterns = [
    path("user-registration/", views.user_registration, name="user_registration"),
    path("", views.user_login, name="user_login"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path('profile/',views.profile,name="profile"),
    path('user-logout/',views.user_logout, name="user_logout"),
    path('password-change2/',views.password_change, name="password_change2"),
    path('signup/',views.signup,name="signup"),


]
