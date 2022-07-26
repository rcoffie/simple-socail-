from django.urls import path

from post_engine import views

urlpatterns = [
    path("index", views.index, name="index"),
    # path('create_post', views.create_post, name="create_post"),
    path("post_detail/<slug:slug>/", views.post_detail, name="post_detail"),
    path("edit-post/<slug:slug>/", views.edit_post, name="edit_post"),
    path("delete-post/<int:pk>/", views.delete_post, name="delete_post"),
    path("edit-comment/<slug:slug>/", views.edit_comment, name="edit_comment"),
    path("delete-comment/<int:pk>/", views.delete_comment, name="delete_comment"),
    path("like/<slug:slug>", views.like, name="like"),
    path('search-user/',views.search_user, name='search_user'),
    path('like-comment/<slug:comment_slug>/post/<slug:post_slug>/',views.like_comment,name="like_comment")
]
