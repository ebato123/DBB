from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Comment

def main (request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        if(request.POST.get('user_name') != "" and request.POST.get('tittle') != "" and request.POST.get('text') != ""):
            Comment.objects.create(
                user_name = request.POST.get('user_name'),
                tittle = request.POST.get('tittle'),
                text = request.POST.get('text')
                )
            messages.success(request, "¡Comentario subido!")
        else:
            messages.error(request, "ERROR: Debes completar todos los campos")
            return render (request, 'pages/comments.html')
            
    return render (request, 'main.html', {'comments':comments})

def comments (request):
    return render (request, 'pages/comments.html')

def projects (request):
    return render (request, 'pages/projects.html')

def loginPage (request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f"MENSAJE: ¡Bienvenid@ {username}!")
                return redirect('/')
            
        messages.error(request,"ERROR: Usuario o contraseña incorrectos.")                
    return render (request, 'pages/login.html')