# Generated by Django 4.0.4 on 2022-10-29 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas_APP', '0003_alter_reservas_hora_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='estado_reserva',
            field=models.CharField(choices=[('Reservado', 'RESERVADO'), ('Completado', 'COMPLETADA'), ('Anulada', 'ANULADA'), ('No Asisten', 'NO ASISTEN')], max_length=10),
        ),
    ]
