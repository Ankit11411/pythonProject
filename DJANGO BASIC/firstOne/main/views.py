from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import ToDoList,Item

# Create your views here.


def display(request,name):
    ls = ToDoList.objects.get(name=name)
    return HttpResponse("<h1>%s<h1>"%ls.name)

def home(request):
    return HttpResponse("<h1>HOMOMOMO<h1>")