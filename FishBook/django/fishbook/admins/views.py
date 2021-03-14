from django.shortcuts import render

def adminIndex(request):
    return render(request, 'admins/adminIndex.html')

def adminLogin(request):
    return render(request, 'admins/adminLogin.html')
# Create your views here.
