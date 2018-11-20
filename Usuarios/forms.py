from django import forms
from .models import PerrosRescatados
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    name_user = forms.CharField(max_length=20,required=True,label="",widget=(forms.TextInput(attrs={"placeholder":"@Usuario","class":"input-login"})))
    password_user = forms.CharField(max_length=20,required=True,label="",widget=(forms.PasswordInput(attrs={"placeholder":"@Contraseña","class":"input-login"})))

class FiltroPerro(forms.Form):
    ESTADOS = (('A','Adoptado'),('R','Rescatado'),('D','Disponible'))
    estado = forms.ChoiceField(choices=ESTADOS)
    
    class Meta:
         fields = ('estado')

class SignUpForm(UserCreationForm):
    CorreoElectronico = forms.EmailField(max_length=100, required=True)
    Run = forms.CharField(max_length=10,required=True)
    NombreUser = forms.CharField(max_length=100,required=True)
    ApellidoUser = forms.CharField(max_length=100,required=True)
    FechaNacimiento = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}),required=True)
    TIPOVIVIENDA = (('CPG','Casa con patio grande'),('CPP','Casa con patio pequeño'),('CSP','Casa sin patio'),('DEP','Departamento'))
    TipoVivienda = forms.ChoiceField(choices=TIPOVIVIENDA)

    class Meta:
        model = User
        fields = ('username', 'FechaNacimiento', 'password1', 'password2','Run','NombreUser','ApellidoUser','CorreoElectronico','TipoVivienda')