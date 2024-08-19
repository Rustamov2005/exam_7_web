from django.shortcuts import render, redirect
from django.views import View
import requests
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username oldin royxatdan otgan')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login( request, user)
            return redirect('loging')
    return render(request, 'main/register.html')

def loging(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Login yoki parol noto\'g\'ri')
        else:
            messages.error(request, 'Iltimos, username va parolni kiriting')
    return render(request, 'main/login.html')

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('loging'))



class XizmatlarView(View):
    def get(self, request):
        headers = {
            'Authorization': 'Token 542223ccc06f3c249e9f4d754e444db1e1b54630',
            'Accept': 'application/json',
        }
        artecle = requests.get( "http://127.0.0.1:8001/articles/").json()
        try:
            response = requests.get("http://127.0.0.1:8001/teams/")
            response.raise_for_status()
            teams = response.json()
        except requests.RequestException as e:
            teams = []
            print(f"API so'rovi xatosi: {e}")

        try:
            response = requests.get("http://127.0.0.1:8001/commites/")
            response.raise_for_status()
            commites = response.json()
        except requests.RequestException as e:
            commites = []
            print(f"API so'rovi xatosi: {e}")
        response = requests.get("http://127.0.0.1:8001/xizmatlar/", headers=headers).json()
        context = {
            'xizmatlar': response,
            'artecle': artecle,
            'teams': teams,
            'commites': commites
        }
        return render(request, 'index.html', context)

def servises(request):
    response = requests.get("http://127.0.0.1:8001/xizmatlar/").json()
    context = {
        'xizmatlar': response,
    }
    return render(request, 'service.html', context)

def abouts(request):
    try:
        response = requests.get("http://127.0.0.1:8001/teams/")
        response.raise_for_status()
        teams = response.json()
    except requests.RequestException as e:
        teams = []
        print(f"API so'rovi xatosi: {e}")

    try:
        response = requests.get("http://127.0.0.1:8001/commites/")
        response.raise_for_status()
        commites = response.json()
    except requests.RequestException as e:
        commites = []
        print(f"API so'rovi xatosi: {e}")
    context = {
        'teams': teams,
        'commites': commites
    }
    return render(request, 'about.html', context)


def contacts(request):
    return render(request, 'contact.html')




# class ArticleView(View):
#     def get(self, request):
#         article = request.get("http://127.0.0.1:8001/articles/").json()
#         context = {
#             'article': article
#         }
#         return render(request, 'login.html', context)
