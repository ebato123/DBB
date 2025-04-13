from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from EXE.methods import check_fields_post_comment, check_fields_register


from .models import Comment

def main (request):
    if request.user.is_authenticated: 
        context = { 'comments': Comment.objects.filter(user_name=request.user.username) }
        return render (request, 'main.html', context)
    else:
        return redirect('/login')

def post_comment(request):
    if request.user.is_authenticated:
        comments = Comment.objects.filter(public=True)
        context = { 'comments':  comments }
        def alignComments():
            last_comment_username = ""
            i = 0
            for comment in comments:
                if i == 0:
                    last_comment_username = comment.user_name
                    i += 1
                if comment.user_name == last_comment_username:
                    comment.comment_align_class = "align-self-start"
                    last_comment_username = comment.user_name
                else: 
                    comment.comment_align_class = "align-self-end"
        
        if request.method == 'POST':
            username = request.user.username
            tittle = request.POST.get('tittle', '').strip()
            text = request.POST.get('text', '').strip()
            public = False if request.POST.get('public-checkbox') == None else True

            if check_fields_post_comment(request, text):
                Comment.objects.create(
                    user_name=username,
                    tittle=tittle if tittle else '', 
                    text=text,
                    public=public
                )
                comments = Comment.objects.filter(public=True)
                context = { 'comments':  comments }
                messages.success(request, "¡Comentario subido!")
                alignComments()
                return render(request,'pages/post_comment.html', context)
            else: 
                context.update({
                    'tittle': tittle,
                    'text': text
                })
        alignComments()
        return render(request, 'pages/post_comment.html', context)
    else:
        return redirect('/login')

def login_page (request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {
            "username": username
        }
        if User.objects.filter(username=username):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f"MENSAJE: ¡Bienvenid@ {username}!")
                return redirect('/')
            else:
                messages.error(request,"ERROR: Usuario o contraseña incorrectos.")
                return render (request, 'pages/login.html', context)   
        else:
                messages.error(request,f"ERROR: No existe el usuario '{username}'")
                return render (request, 'pages/login.html', context)   
        
    if request.user.is_authenticated:
        logout(request)
        messages.warning(request, 'MENSAJE: Cerraste sesión')
        return redirect('/')
    else:
        return render (request, 'pages/login.html')
    
def register_page (request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirm_password')
        email = request.POST.get('email')
        firstName =  request.POST.get('first_name')
        lastName =  request.POST.get('last_name')
        context = {
                'email': email,
                'username': username,
                'first_name': firstName,
                'last_name': lastName
            }
        
        if(check_fields_register(request,email,username,password,confirmPassword)):
            user = User(username=username, email=email, last_name=lastName, first_name=firstName)
            user.set_password(password)
            user.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f"MENSAJE: ¡Bienvenid@ {username}!")
                return redirect('/')
            else:
                messages.error(request,"ERROxR: No se pudo crear el usuario, intente nuevamente.")
                return render (request, 'pages/register.html', context)                   
        else:
            return render (request, 'pages/register.html', context)
    return render (request, 'pages/register.html')
