from django.shortcuts import render, redirect
from post_engine.forms import PostInfoForm
from post_engine.models import PostInfo

# Create your views here.
def index(request):
    posts = PostInfo.objects.all()
    form = PostInfoForm()
    if request.method == 'POST':
        form = PostInfoForm(request.POST, request.FILES)
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


def post_detail(request, pk):
    posts = PostInfo.objects.filter(id=pk)
    context = {'posts':posts}
    return render(request, 'post_engine/post_detail.html', context)
