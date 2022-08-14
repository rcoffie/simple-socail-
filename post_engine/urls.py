from django.urls import path
from post_engine import views

urlpatterns = [
     path("index", views.index, name="index"),
     # path('create_post', views.create_post, name="create_post"),
     path('post_detail/<str:pk>/', views.post_detail, name="post_detail"),
     path('edit-post/<int:pk>/',views.edit_post,name="edit_post"),
     path('delete-post/<int:pk>/',views.delete_post,name="delete_post"),
     path('edit-comment/<int:pk>/',views.edit_comment,name="edit_comment"),
     path('delete-comment/<int:pk>/',views.delete_comment, name='delete_comment')
]
