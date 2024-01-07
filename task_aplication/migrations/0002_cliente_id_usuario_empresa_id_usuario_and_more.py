# Generated by Django 4.2.6 on 2023-11-13 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("task_aplication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="id_usuario",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="task_aplication.usuario",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="empresa",
            name="id_usuario",
            field=models.ForeignKey(
                default=int,
                on_delete=django.db.models.deletion.CASCADE,
                to="task_aplication.usuario",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="publicista",
            name="id_usuario",
            field=models.ForeignKey(
                default=25,
                on_delete=django.db.models.deletion.CASCADE,
                to="task_aplication.usuario",
            ),
            preserve_default=False,
        ),
    ]