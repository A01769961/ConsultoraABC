from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
import datetime
from django.contrib import messages
from .models import *
from django.core import validators
from django.core.validators import RegexValidator


letras = RegexValidator(r'^[a-zA-Z " " éáíóúñÑÁÉÍÓÚ]*$', 'Solo se pueden ingresar letras ')
numeros = RegexValidator(r'^[0-9]*$', 'Solo se pueden ingresar numeros')
numerosYletras = RegexValidator(r'^[0-9a-zA-Z " "éáíóúñÑÁÉÍÓÚ]*$', 'Solo se pueden ingresar numeros y letras')

roles = (
    ("ADM", "Administrador"),
    ("CLI", "Cliente"),
    ("CON", "Consultor"),
    ("OFG", "Oficinas generales"),
)

class signup(forms.Form):
    
    name = forms.CharField( max_length = 40, 
                            required = True, 
                            label = "Nombre(s)",
                            validators=[letras],
                            error_messages={
                                "required": "No puede estar vacío",
                            },
                            widget = forms.TextInput(attrs = {
                                "class": "form-control"
                                }
                            ))

    lastName = forms.CharField( max_length = 40, 
                                required = True, 
                                label = "Apellido Paterno",
                                validators=[letras],
                                error_messages={
                                    "required": "No puede estar vacío",
                                },
                                widget = forms.TextInput(attrs = {
                                    "class": "form-control"
                                    }
                                ))

    momLastName = forms.CharField(  max_length = 40, 
                                    required = True, 
                                    validators=[letras],
                                    error_messages={
                                        "required": "No puede estar vacío",
                                    },
                                    label = "Apellido Materno",
                                    widget = forms.TextInput(attrs = {
                                        "class": "form-control"
                                        }
                                    ))
    
    email = forms.EmailField(
        initial = 'Escribe tu correo electronico', 
        required=True, 
        validators=[validators.EmailValidator(message="Correo no valido")]
        )
    
    password = forms.CharField(
        widget=forms.PasswordInput,
         max_length = 8,
        required=True, 
        validators=[numerosYletras],
        error_messages={"required": "No puede estar vacío",},
        label = "Contraseña",
    )

    rol = forms.ChoiceField(required = True,
                            choices = roles,
                            label = "Selecciona tu rol: ",
                            widget = forms.Select(attrs = {
                                "class": "form-control",
                                },)
    )

    def clean_name(self):
        name = self.cleaned_data.get("name")   
        name = name.replace("á" , "a")
        name = name.replace("é" , "e")
        name = name.replace("í" , "i")
        name = name.replace("ó" , "o")
        name = name.replace("ú" , "u")
        name = name.replace("ñ" , "nh")
        name = name.replace("Á" , "A")
        name = name.replace("É" , "E")
        name = name.replace("Í" , "I")
        name = name.replace("Ó" , "O")
        name = name.replace("Ú" , "Ú")
        name = name.replace("Ñ" , "Nh")
        return name

    def clean_lastName(self):
        lastName = self.cleaned_data.get("lastName")  
        lastName = lastName.replace("á" , "a")
        lastName = lastName.replace("é" , "e")
        lastName = lastName.replace("í" , "i")
        lastName = lastName.replace("ó" , "o")
        lastName = lastName.replace("ú" , "u")
        lastName = lastName.replace("ñ" , "nh")
        lastName = lastName.replace("Á" , "A")
        lastName = lastName.replace("É" , "E")
        lastName = lastName.replace("Í" , "I")
        lastName = lastName.replace("Ó" , "O")
        lastName = lastName.replace("Ú" , "Ú")
        lastName = lastName.replace("Ñ" , "Nh")
        return lastName

    def clean_momLastName(self):
        momLastName = self.cleaned_data.get("momLastName")   
        momLastName = momLastName.replace("á" , "a")
        momLastName = momLastName.replace("é" , "e")
        momLastName = momLastName.replace("í" , "i")
        momLastName = momLastName.replace("ó" , "o")
        momLastName = momLastName.replace("ú" , "u")
        momLastName = momLastName.replace("ñ" , "nh")
        momLastName = momLastName.replace("Ñ" , "Nh")
        momLastName = momLastName.replace("Á" , "A")
        momLastName = momLastName.replace("É" , "E")
        momLastName = momLastName.replace("Í" , "I")
        momLastName = momLastName.replace("Ó" , "O")
        momLastName = momLastName.replace("Ú" , "Ú")
        momLastName = momLastName.replace("Ñ" , "Nh")
        return momLastName
    
    def clean_mail(self):
        mail = self.cleaned_data.get("mail")
        if (mail == ""):  
            raise forms.ValidationError("Introduce al menos un metodo de contacto")  
        return mail 


class LoginForm(forms.Form):
    correo = forms.CharField(label="",
                                max_length=18,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Correo',
                                    "class": "form-control"
                                    }),
                                )
    password = forms.CharField(label="",
                                max_length=18,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'contraseña',
                                    "class": "form-control"
                                    }),
                                )

    def clean_user(self):

        correo = self.cleaned_data.get("correo")
        password = self.cleaned_data.get("password")

        try:
            user = usuario.objects.get(mail=correo)
            print(user)
            return user

        except usuario.DoesNotExist:
            raise forms.ValidationError("El usuario no existe")
    
