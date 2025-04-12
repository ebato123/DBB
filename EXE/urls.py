from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('post_comment/', views.post_comment),
    path('login/', views.login_page),
    path('register/', views.register_page),
]