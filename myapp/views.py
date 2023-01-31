from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h4>Hello World!</h4><a href='about/'> About</a>")

def about(request):
    return HttpResponse("<p>About</p><a href='/' >volver</a>")