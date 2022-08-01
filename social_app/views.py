import imp
from django.shortcuts import render
from django.shortcuts import redirect
from social_app.models import Post
from social_app.forms import PostForm
from django.contrib.auth import logout


# Create your views here.

def index(request):
    post_list = Post.objects.all()
    context ={'post_list':post_list}
    return render(request, 'index.html', context)




def write_post(request):
    post_form = PostForm()
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
           temp_post =  post.save(commit=False)
           temp_post.user = request.user
           temp_post.save()
           return redirect('index')
    context = {'post_form' : post_form}
    return render(request, 'post_engine/write_post.html', context)
