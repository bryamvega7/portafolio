from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return redirect ('portafolio')

def registerUser(request):

    if request.method == 'GET':
        return render(request, 'register.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('portafolio')
            except IntegrityError:
                return render(request, 'register.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists'
                })

        return render(request, 'register.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

def loginUser(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('proyectos')


        
@login_required    
def logoutUser(request):
    logout(request)
    return redirect('login')

