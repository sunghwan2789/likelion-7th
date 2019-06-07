from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],password=request.POST["password1"]
            )
            return render(request, 'signup_done.html')
        raise ValueError ('비밀번호와 비밀번호 확인란의 값이 일치하지 않습니다')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('main')
        raise ValueError ('아이디와 비밀번호가 일치하지 않습니다.')
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def logout(request):
    # if request.method == 'POST':
    #     auth.logout(request)
    #     return redirect('main')
    # return render(request,'login.html')
    auth.logout(request)
    return redirect('main')
def mypage(request):
    return render(request, 'mypage.html')

