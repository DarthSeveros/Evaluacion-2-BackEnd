# Generated by Django 4.0.4 on 2022-10-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_reserva', models.DateField()),
                ('hora_reserva', models.DateTimeField()),
                ('cantidad_personas', models.IntegerField()),
                ('estado_reserva', models.CharField(choices=[('reservado', 'RESERVADO'), ('completado', 'COMPLETADA'), ('anulada', 'ANULADA'), ('no asisten', 'NO ASISTEN')], max_length=10)),
                ('observacion', models.CharField(blank=True, max_length=120)),
            ],
        ),
    ]
