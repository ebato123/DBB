from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
# Create your views here.

def main (request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        Comment.objects.create(
            user_name = request.POST.get('user_name'),
            tittle = request.POST.get('tittle'),
            text = request.POST.get('text')
        )
    return render (request, 'main.html', {'comments':comments})

def comments (request):
    return render (request, 'pages/comments.html')

def projects (request):
    return render (request, 'pages/projects.html')