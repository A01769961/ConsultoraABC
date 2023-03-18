from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path('home/', views.home, name='home'),
    path("login", views.login, name = "login"),

    path("signup", views.signupU, name = "signup"),
    path("consultores", views.consultoresMain, name = "consultores"),
    path("oficina", views.oficinasMain, name = "oficinas"),

]