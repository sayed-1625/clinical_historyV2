# Generated by Django 3.2 on 2022-11-23 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaCita', models.CharField(max_length=20)),
                ('TensionArterial', models.CharField(max_length=20)),
                ('Saturacion', models.CharField(max_length=20)),
                ('Temperatura', models.CharField(max_length=20)),
                ('HabitosDeRiesgo', models.CharField(max_length=20)),
                ('Persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='person.persona')),
            ],
            options={
                'verbose_name': 'paciente',
                'verbose_name_plural': 'pacientes',
            },
        ),
    ]