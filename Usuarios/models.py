from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class PerrosRescatados(models.Model):
    Fotografia = models.ImageField(upload_to="Usuarios/media/imagenesPerros/")
    NombrePerro = models.CharField(max_length=200)
    RazaPredominante = models.CharField(max_length=200)
    Descripcion = models.TextField()
    ESTADOS = (('R','Rescatado'),('D','Disponible'),('A','Adoptado'))
    Estado = models.CharField(max_length=1,choices=ESTADOS,default='R')
    
    def __str__(self):
        return self.NombrePerro

class Regiones(models.Model):
    region = models.CharField(max_length=200)
    
    def __str__(self):
        return self.region

class Comunas(models.Model):
    comunas = models.ForeignKey(Regiones,on_delete=models.CASCADE)
    nombreComuna = models.CharField(max_length=500)

    def __str__(self):
        return self.nombreComuna   

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    CorreoElectronico = models.CharField(max_length=100)
    Run = models.CharField(max_length=10)
    NombreUser = models.CharField(max_length=100)
    ApellidoUser = models.CharField(max_length=100)
    FechaNacimiento = models.DateField(null=True)
    Region = models.ForeignKey(Regiones, on_delete=models.SET_NULL, null=True)
    Comuna = models.ForeignKey(Comunas, on_delete=models.SET_NULL, null=True) 
    TIPOVIVIENDA = (('CPG','Casa con patio grande'),('CPP','Casa con patio pequeño'),('CSP','Casa sin patio'),('DEP','Departamento'))
    TipoVivienda = models.CharField(max_length=3,choices=TIPOVIVIENDA,default='CPG')

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)
    instance.profile.save()
    