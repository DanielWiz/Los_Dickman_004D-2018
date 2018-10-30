from django.shortcuts import render, HttpResponse

def inicio(request):
    return render(request, 'usuarios/inicio.html')

def login(request):
    return render(request, 'usuarios/login.html')     