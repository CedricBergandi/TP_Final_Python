# Generated by Django 4.1.7 on 2023-05-03 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_autoridades_femenino_profesional_reserva_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='puesto',
            field=models.CharField(default='N/A', max_length=50),
            preserve_default=False,
        ),
    ]