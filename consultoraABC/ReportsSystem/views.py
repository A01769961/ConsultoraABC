from django.shortcuts import render
from django.contrib.auth import logout, login
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.forms import formset_factory
from bson import ObjectId
from datetime import datetime
import string
import random
import shortuuid

from .forms import *
from .models import *
#https://learndjango.com/tutorials/django-custom-user-model

def home(request,*args, **kwargs):
    print(request)
    # return render(request, "registration/login.html")
    # #return HttpResponse("<h1>Hello World</h1>")
    # if request.user.is_authenticated:
    #     return render(request, "census/home.html")
    
    return redirect("login")


def login(request):

    loginForm = LoginForm()
    context = {
        "form": loginForm
    }

    if request.method == "POST":

        loginForm = LoginForm(request.POST)
        context = {
            "form": loginForm
        }

        if loginForm.is_valid():
            print("Valid")
            print(request.POST)
            data = loginForm.cleaned_data
            userMail = data["correo"] 
            contrasenia = data["password"] 
            print(userMail)
            print(contrasenia)
            
            Umail = usuario.objects.filter(mail = userMail, contrasenia=contrasenia)
            
            if Umail.exists():
                uData = usuario.objects.filter(mail = userMail)
                print(uData[0])
                print("logs in")
                return redirect("consultores")
            else:
                print("not log in")
                return render(request, "registration/login.html", context)
        else:
            print("Invalid")
            print(request.POST)

            return render(request, "registration/login.html", context)
    else:
        return render(request, "registration/login.html", context)
    

def consultoresMain(request):
    print(request)
    # return render(request, "registration/login.html")
    # #return HttpResponse("<h1>Hello World</h1>")
    # if request.user.is_authenticated:
    #     return render(request, "census/home.html")
    
    #return redirect("consultores")
    return render(request, "registration/consultores.html")

def oficinasMain(request):
    print(request)
    # return render(request, "registration/login.html")
    # #return HttpResponse("<h1>Hello World</h1>")
    # if request.user.is_authenticated:
    #     return render(request, "census/home.html")
    
    #return redirect("consultores")
    return render(request, "registration/consultores.html")


def signupU(request):
    print("----------- entered signup -----------")
    print(request)

    if request.method == "POST":
        print("enter post")
        signup_form = signup(request.POST)
        context = {
            "title": "Registro de usuarios",
            "form": signup_form
        }

        if signup_form.is_valid():
            print("FORM VALID!")

            data = signup_form.cleaned_data

            
            
            print("data:\n",data)
            m = data["email"]
            #print(usuario.objects.filter(mail="a01360000@tec.mx"))
            if User.objects.filter(email = data['email']).exists():
                print("Mail existe")
                messages.error(request, "Este correo ya fue usado")
            else:
                print("no existe")
                try:
                    print("create success")

                    usuario.objects.create(
                        #id = unique_id(8),
                        name = data["name"],
                        PlastName = data["lastName"],
                        MLastName = data["momLastName"],
                        mail = data["email"],
                        contrasenia = data["password"],
                        rol = data["rol"],
                    )
                    
                    messages.success(request, "Datos guardados correctamente")

                    return redirect("login")
            
                except:
                    print("creare failed")
                    messages.error(request, "Error al guardar los datos")
            
            
    
        return render(request, "registration/registro.html", context)
    
    else:
        print("no post")
        signup_form = signup()
        context = {
            "title": "Registro de Usuarios",
            "form": signup_form
        }

        return render(request, "registration/registro.html", context)