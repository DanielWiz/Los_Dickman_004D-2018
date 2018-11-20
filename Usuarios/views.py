from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render 
from django.contrib.auth.forms import UserCreationForm
from .models import PerrosRescatados
from .forms import SignUpForm,FiltroPerro

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.FechaNacimiento = form.cleaned_data.get('FechaNacimiento')
            user.profile.Run = form.cleaned_data.get('Run')
            user.profile.Nombreuser = form.cleaned_data.get('Nombreuser')
            user.profile.Apellidouser = form.cleaned_data.get('Apellidouser')
            user.profile.Correelectronico = form.cleaned_data.get('Correoelectronico')
            user.profile.Tipovivienda = form.cleaned_data.get('TipoVivienda')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            return HttpResponseRedirect('/') 
    else:
        form = SignUpForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def inicio(request):
    return render(request, 'usuarios/inicio.html')

def login(request):
    return render(request, 'usuarios/login.html')     

def adopcion(request):
    if request.method == 'POST':
        form = FiltroPerro(request.POST)
        if form.is_valid():
           filtro = form.cleaned_data['estado']
           form.save()
           return HttpResponseRedirect('/adopcion')
        else:
            return HttpResponseRedirect('/adopcion')     
    else:
        form = FiltroPerro()
        args1 = {'form' : form}
        perros = PerrosRescatados.objects.all()
        return render(request, 'usuarios/adopcion.html',{'perros': perros},args1)
         

def logout(request):
    return render(request, 'usuarios/logout.html')     
 
            


