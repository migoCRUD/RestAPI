# Generated by Django 4.2.6 on 2024-01-07 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "task_aplication",
            "0006_alter_usuario_contrasena_alter_usuario_email_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="campanapublicitaria",
            name="id_sector",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="formularioregistrocampana",
            name="licencia",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="formularioregistrocampana",
            name="matricula",
            field=models.ImageField(upload_to="images/"),
        ),
    ]