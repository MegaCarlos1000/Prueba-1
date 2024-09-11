from django.shortcuts import render
from django.http import HttpResponse





def display1(request):
    data = {"Raza":"Tipos de perro",}
    return request("templatesapp/primer_2.html",data)

def display2(request):
    data = {"Raza":"Raza",}
    return request("templatesapp/primer_2.html",data)

def display3(request):
    data = {"Raza":"Quiltro"}
    return request("templatesapp/primer_2.html",data)

def display4(request):
    data = {"Raza":"Mesclas"}
    return request("templatesapp/primer_2.html",data)