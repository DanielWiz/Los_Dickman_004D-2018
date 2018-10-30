from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render 
from django.contrib.auth.forms import UserCreationForm

def inicio(request):
    return render(request, 'usuarios/inicio.html')

def login(request):
    return render(request, 'usuarios/login.html')     

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inicio')
        else:
            return HttpResponseRedirect('/')    
    else:
        form = UserCreationForm()
        args = {'form' : form}
        return render(request, 'usuarios/registro.html', args)        


