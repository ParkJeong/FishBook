from django.shortcuts import render

def index(request):
    return render(request, 'posts/index.html')

def goFishing(request):
    return render(request, 'posts/go-fishing.html')

def join(request):
    return render(request, 'posts/join.html')

def login(request):
    return render(request, 'posts/login.html')

# Create your views here.
