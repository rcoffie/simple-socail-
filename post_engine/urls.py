from django.urls import path
from post_engine import views

urlpatterns = [
     path("index", views.index, name="index"),
     # path('create_post', views.create_post, name="create_post"),
     path('post_detail/<str:pk>/', views.post_detail, name="post_detail"),
     path('edit-post/<int:pk>/',views.edit_post,name="edit_post"),
     path('delete-post/<int:pk>/',views.delete_post,name="delete_post"),
     path('post-comment/<int:pk>/',views.post_comment,name="post_comment"),

]
