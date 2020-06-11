from django.shortcuts import render, redirect
from .forms import PostForm

def index(request):
    return render(request, 'posts/index.html')

def goFishing(request):
    return render(request, 'posts/goFishing.html')

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
