from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import User
from django.forms import model_to_dict
import pdb

def joinform(request):
    return render(request, 'users/joinform.html')

def joinsuccess(request):
    return render(request, 'users/joinsuccess.html')

def join(request):
    user = User()
    user.email = request.POST.get('email')
    user.userPw = request.POST.get('pw')
    if user.email != None and user.userPw != None:
        user.save()
    return HttpResponseRedirect(reverse('users:joinsuccess'))
    # return render(request, 'users/join.html')


def checkemail(request):
    try:
        user = User.objects.get(email=request.GET.get('email'))
    except Exception as e:
        user = None
    result = {
        'result':'success',
        # 'data' : model_to_dict(user)  # console에서 확인
        'data' : "not exist" if user is None else "exist"
    }

    return JsonResponse(result)

def loginform(request):
    return render(request, 'users/loginform.html')

def login(request):
    results = User.objects.filter(email=request.POST.get('email')).filter(userPw=request.POST.get('pw'))

    if len(results) == 0:
        return HttpResponseRedirect('/users/loginform?result=fail')

    authUser = results[0]
    request.session['authUser'] = model_to_dict(authUser)

    return HttpResponseRedirect('/')

def logout(request):
    del request.session['authUser']
    return HttpResponseRedirect('/')

def updateform(request):
    user = User.objects.get(email=request.session['authUser']['email'])
    data = {
        'user': user
    }
    return render(request, 'users/updateform.html', data)

def update(request):
    user = User.objects.get(email=request.session['authUser']['email'])

    if request.POST.get('pw') == user.userPw:
        pass
    else:
        return HttpResponseRedirect('/users/updateform?result=fail')

    if request.POST.get('new_pw') != '':
        user.userPw = request.POST.get('new_pw')
    user.save()

    return HttpResponseRedirect('/users/updateform?result=success')
# Create your views here.
