# Generated by Django 4.2.6 on 2024-01-08 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_aplication", "0012_alter_vehiculo_color_vehiculo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehiculo",
            name="categoria_vehiculo",
            field=models.CharField(
                choices=[
                    ("sedan", "Sedan"),
                    ("suv", "SUV"),
                    ("camioneta", "Camioneta"),
                    ("camion", "Camion"),
                    ("bus", "Bus"),
                ],
                max_length=20,
            ),
        ),
    ]
