from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def hello(request, nombreUsuario):
    print(nombreUsuario)
    return HttpResponse("<h1>Hello %s</h1>" %nombreUsuario)

def about(request):
    return HttpResponse("about")

