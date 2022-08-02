from django.shortcuts import render, redirect
from post_engine.forms import PostInfoForm
from post_engine.models import PostInfo

# Create your views here.
def index(request):
    posts = PostInfo.objects.all()
    context = {'posts':posts}
    return render(request, "index.html", context)


def create_post(request):
    postform = PostInfoForm()
    if request.POST:
        form_check = PostInfoForm(request.POST, request.FILES)
        if form_check.is_valid():
            check = form_check.save(commit=False)
            check.user = request.user
            check.save()
            return redirect('index')
        return redirect('create_post')    
    context = {'postform': postform}
    return render(request, 'post_engine/create_post.html', context)


def post_detail(request, pk):
    posts = PostInfo.objects.filter(id=pk)
    context = {'posts':posts}
    return render(request, 'post_engine/post_detail.html', context)