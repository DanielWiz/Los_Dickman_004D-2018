from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate 
from django.contrib.auth.forms import UserCreationForm
from .models import PerrosRescatados
from .forms import SignUpForm,FiltroPerro

def RegistroDatos(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('FechaNacimiento')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/login')
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
 
def detalle_perro(request, pk):
    perros = get_object_or_404(PerrosRescatados, pk=pk)
    return render(request, 'usuarios/perros_detalles.html', {'perros': perros})            


