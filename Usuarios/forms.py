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
    YEARS= [x for x in range(1900,2018)]
    FechaNacimiento = forms.DateField(widget=forms.SelectDateWidget(years=YEARS),required=True)
    TIPOVIVIENDA = (('CPG','Casa con patio grande'),('CPP','Casa con patio pequeño'),('CSP','Casa sin patio'),('DEP','Departamento'))
    TipoVivienda = forms.ChoiceField(choices=TIPOVIVIENDA)

    class Meta:
        model = User
        fields = ('username', 'FechaNacimiento', 'password1', 'password2','Run','NombreUser','ApellidoUser','CorreoElectronico','TipoVivienda')

    def save(self,commit = True):
         user = super(SignUpForm, self).save(commit = False)
         user.username = self.cleaned_data['username']
         user.password1 = self.cleaned_data['password1']
         user.CorreoElectronico = self.cleaned_data['CorreoElectronico']
         user.Run = self.cleaned_data['Run']
         user.NombreUser = self.cleaned_data['NombreUser']
         user.ApellidoUser = self.cleaned_data['ApellidoUser']
         user.FechaNacimiento = self.cleaned_data['FechaNacimiento']
         user.TipoVivienda = self.cleaned_data['TipoVivienda']
         
         if commit:
             user.save()

         return user    