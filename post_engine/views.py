from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from post_engine.forms import PostForm, CommentForm
from post_engine.models import Post, Comment
from django.contrib import messages
from django.urls import reverse, reverse_lazy
# Create your views here.
def index(request):
    posts = Post.objects.all()
    c_form = CommentForm()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.user = request.user
            save_form.save()
            return redirect('index')

    context = {'posts':posts,'form':form,'c_form':c_form,}
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


def edit_post(request, slug):

    context = {}
    post = Post.objects.get(slug=slug)
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

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    total_comments = comments.count()

    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            body = request.POST['body']
            user = request.user
            save_form = Comment.objects.create(body=body,user=user,post=post)
            save_form.save()
            messages.success(request, 'comment added')
            return HttpResponseRedirect(reverse("post_detail", args=[post.slug]))
    else:
        form = CommentForm()

    context = {'post':post,'comments':comments,'form':form,'total_comments':total_comments,'is_liked':is_liked,'total_likes':post.get_total_likes()}
    return render(request, 'post_engine/post_detail.html', context)


def edit_comment(request, slug):
    comment = get_object_or_404(Comment, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'comment edited')
            return HttpResponseRedirect(reverse("edit_comment", args=[comment.slug]))
    else:
        form = CommentForm(instance=comment)
    context = {'form':form,}
    return render( request, 'post_engine/edit_comment.html',context)


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    messages.warning(request, 'comment deleted')
    return redirect('index')

def like(request, pk):
    post = get_object_or_404(Post,pk=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked =True

    return HttpResponseRedirect(reverse("post_detail", args=[post.id]))
