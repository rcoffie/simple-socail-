from django.urls import path
from social_app import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('write_post/', views.write_post, name="write_post"),
]
