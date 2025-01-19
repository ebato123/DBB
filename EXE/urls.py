from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('comments/', views.comments),
    path('projects/', views.projects),
]