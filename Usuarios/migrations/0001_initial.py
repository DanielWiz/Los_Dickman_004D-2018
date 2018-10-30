# Generated by Django 2.0.9 on 2018-10-30 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreComuna', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CorreoElectronico', models.CharField(max_length=100)),
                ('Run', models.CharField(max_length=10)),
                ('NombreUser', models.CharField(max_length=100)),
                ('ApellidoUser', models.CharField(max_length=100)),
                ('FechaNacimiento', models.DateField()),
                ('TipoVivienda', models.CharField(choices=[('CPG', 'Casa con patio grande'), ('CPP', 'Casa con patio pequeño'), ('CSP', 'Casa sin patio'), ('DEP', 'Departamento')], default='CPG', max_length=3)),
                ('Comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Usuarios.Comunas')),
            ],
        ),
        migrations.CreateModel(
            name='Regiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='perfilusuario',
            name='Region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Usuarios.Regiones'),
        ),
        migrations.AddField(
            model_name='perfilusuario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comunas',
            name='comunas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Regiones'),
        ),
    ]
