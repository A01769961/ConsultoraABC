from django.http import HttpResponse

#https://learndjango.com/tutorials/django-login-and-logout-tutorial
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")