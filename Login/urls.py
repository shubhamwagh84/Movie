"""Movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Login/', views.LoginPage , name='Login Page'),
    path('Signup/', views.SignupPage , name='Signup Page'),
    path('Adduser/', views.AddUser , name='AddUser Page'),
    path('Addmovie/',views.AddMovie, name='Movie Add'),
    path('Deletemovie/',views.DeleteMovie, name='Delete Movie'),
    path('Help/',views.Help, name='Help Page'),
    path('AboutUs/', views.AboutUs, name='AboutUs Page'),
    path('Home/',views.Home,name='home Page'),
    path('Viewmovie/',views.ViewMovie,name='ViewMovie Page'),
    path('',views.ViewLogin,name='ViewMovie1 Page'),

]
