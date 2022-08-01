import imp
from django.shortcuts import render
from django.shortcuts import redirect
from social_app.models import Post
from social_app.forms import PostForm
from django.contrib.auth import logout
from account_engine.models import Profile


# Create your views here.

def index(request):
    post_list = Post.objects.all()
    context ={'post_list':post_list}
    return render(request, 'index.html', context)




def write_post(request):
    pro = Profile()
    post_form = PostForm()
    if request.method == 'POST':
        post = PostForm(request.POST, request.FILES)
        if post.is_valid():
           post.save()
           return redirect('index')
    context = {'post_form' : post_form}
    return render(request, 'post_engine/write_post.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render(request, 'post_engine/detail.html', context)



