from django.shortcuts import render
from django.http import HttpResponse

def display1(request):
    return ("<h1>hola")

def display2(request):
    data = {"Raza":"Raza Husky Siberiano",}
    return 