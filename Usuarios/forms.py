from django import forms

from .models import PerrosRescatados

class PerrosPost(forms.ModelForm):

    class Meta:
        model = PerrosRescatados
        fields = ('Foto', 'Nombre', 'Raza','Descripcion','Estado')