# Generated by Django 4.1.7 on 2023-05-06 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_comentario_mensaje_delete_femenino_delete_reserva_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='mensaje',
        ),
        migrations.DeleteModel(
            name='Mensaje',
        ),
    ]
