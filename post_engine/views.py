from django.shortcuts import render, redirect
from post_engine.forms import PostForm
from post_engine.models import Post
from django.contrib import messages
# Create your views here.
def index(request):
    posts = Post.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.user = request.user
            save_form.save()
            return redirect('index')
    context = {'posts':posts,'form':form,}
    return render(request, "index.html", context)


# def create_post(request):
#     form = PostInfoForm()
#     if request.POST:
#         form = PostInfoForm(request.POST, request.FILES)
#         if form.is_valid():
#             save_form = form.save(commit=False)
#             save_form.user = request.user
#             save_form.save()
#             return redirect('index')
#         return redirect('create_post')
#     context = {'form': form}
#     return render(request, 'index.html', context)


def edit_post(request, pk):

    context = {}
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'post_engine/edit_post.html',context)


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    messages.warning(request,'Post deleted ')
    return redirect('index')

def post_detail(request, pk):
    posts = PostInfo.objects.filter(pk=pk)
    context = {'posts':posts}
    return render(request, 'post_engine/post_detail.html', context)
