# Generated by Django 2.0.9 on 2018-11-17 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0005_auto_20181117_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perrosrescatados',
            name='Fotografia',
            field=models.ImageField(upload_to='Usuarios/media/imagenesPerros/'),
        ),
    ]