from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def index(request):
    context = {
        'posts': Post.objects.order_by('-created_at')
    }
    return render(request, 'posts/index.html', context)

def goFishing(request):
    context = {
        'posts': Post.objects.order_by('-created_at')
    }
    return render(request, 'posts/goFishing.html', context)

def join(request):
    return render(request, 'posts/join.html')

def login(request):
    return render(request, 'posts/login.html')

def new(request):
    context = {
        'form': PostForm()
    }
    return render(request, 'posts/new.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect(goFishing)    
# Create your views here.

def show(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/show.html', context)