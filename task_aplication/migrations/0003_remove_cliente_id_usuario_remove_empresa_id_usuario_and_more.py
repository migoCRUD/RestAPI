# Generated by Django 4.2.6 on 2023-11-13 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("task_aplication", "0002_cliente_id_usuario_empresa_id_usuario_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cliente",
            name="id_usuario",
        ),
        migrations.RemoveField(
            model_name="empresa",
            name="id_usuario",
        ),
        migrations.RemoveField(
            model_name="publicista",
            name="id_usuario",
        ),
    ]