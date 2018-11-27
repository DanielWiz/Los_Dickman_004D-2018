from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import UserCreationForm
from .models import PerrosRescatados
from .forms import SignUpForm,FiltroPerro
from django.views.generic import TemplateView

class IndexView(TemplateView):

    template_name = 'login.html'


def RegistroDatos(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.CorreoElectronico = form.cleaned_data.get('CorreoElectronico')
            user.profile.Run = form.cleaned_data.get('Run')
            user.profile.NombreUser = form.cleaned_data.get('NombreUser')
            user.profile.ApellidoUser = form.cleaned_data.get('ApellidoUser')
            user.profile.FechaNacimiento = form.cleaned_data.get('FechaNacimiento')
            user.profile.TipoVivienda = form.cleaned_data.get('TipoVivienda')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'usuarios/registro.html', {'form': form})
            
            

def inicio(request):
    return render(request, 'usuarios/inicio.html')

def logeo(request):
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
    """Logs out user"""
    auth_logout(request)
    return render(request, 'usuarios/inicio.html')  
 
def detalle_perro(request, pk):
    perros = get_object_or_404(PerrosRescatados, pk=pk)
    return render(request, 'usuarios/perros_detalles.html', {'perros': perros})            

def base_layout(request):
	template='base.html'
	return render(request,template)
