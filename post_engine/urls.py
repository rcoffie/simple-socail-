from django.urls import path
from post_engine import views

urlpatterns = [
     path("index", views.index, name="index"),
     # path('create_post', views.create_post, name="create_post"),
     path('post_detail/<str:pk>/', views.post_detail, name="post_detail"),
]

 
