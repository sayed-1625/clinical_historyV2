# Generated by Django 3.2 on 2022-11-10 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20221109_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='is_active',
            new_name='usuario_activo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario_administrador',
            field=models.BooleanField(default=False),
        ),
    ]
