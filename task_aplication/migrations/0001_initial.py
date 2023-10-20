# Generated by Django 4.2.6 on 2023-10-19 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CampanaPublicitaria",
            fields=[
                ("id_campana", models.AutoField(primary_key=True, serialize=False)),
                ("nombre_campana", models.CharField(max_length=20)),
                ("fecha_inicio", models.DateField()),
                ("fecha_fin", models.DateField()),
                ("fecha_fin_registro", models.DateField()),
                ("presupuesto", models.FloatField()),
                ("nombre_responsable", models.CharField(max_length=20)),
                ("tarifa_base", models.FloatField()),
                ("taller_brandeo", models.CharField(max_length=20)),
                ("carroceria_capo", models.BooleanField()),
                ("puerta_conductor", models.BooleanField()),
                ("puerta_pasajero", models.BooleanField()),
                ("puerta_traseratzq", models.BooleanField()),
                ("puerta_traseraDer", models.BooleanField()),
                ("carroceria_guantera", models.BooleanField()),
                ("carroceria_techo", models.BooleanField()),
                ("fecha_creacion", models.DateField()),
                ("fecha_modificacion", models.DateField()),
                ("estado", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Chofer",
            fields=[
                ("id_chofer", models.AutoField(primary_key=True, serialize=False)),
                ("cedula_chofer", models.CharField(max_length=10)),
                ("nombre", models.CharField(max_length=20)),
                ("apellido", models.CharField(max_length=20)),
                ("fecha_nacimiento", models.DateField()),
                ("sexo", models.IntegerField()),
                ("estado", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                ("id_cliente", models.AutoField(primary_key=True, serialize=False)),
                ("cedula_cliente", models.CharField(max_length=10)),
                ("nombre", models.CharField(max_length=20)),
                ("apellido", models.CharField(max_length=20)),
                ("fecha_nacimiento", models.DateField()),
                ("email", models.CharField(max_length=40)),
                ("sexo", models.IntegerField()),
                ("telefono", models.CharField(max_length=10)),
                ("estado", models.IntegerField()),
                (
                    "id_campana",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.campanapublicitaria",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Empresa",
            fields=[
                ("id_empresa", models.AutoField(primary_key=True, serialize=False)),
                ("ruc", models.CharField(max_length=13)),
                ("nombre", models.CharField(max_length=30)),
                ("descripcion", models.CharField(max_length=50)),
                ("mail_contacto", models.CharField(max_length=40)),
                ("telefono", models.CharField(max_length=10)),
                ("fecha_creacion", models.DateField()),
                ("fecha_modificacion", models.DateField()),
                ("estado", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="MarcasVehiculos",
            fields=[
                ("id_marca", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("id_menu", models.AutoField(primary_key=True, serialize=False)),
                ("estado", models.IntegerField()),
                ("nombre_menu", models.CharField(max_length=40)),
                ("descripcion", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="ModelosVehiculos",
            fields=[
                ("id_modelo", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=30)),
                (
                    "id_marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.marcasvehiculos",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notificacion",
            fields=[
                (
                    "id_notificacion",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("fecha_creacion", models.DateField()),
                ("fecha_fin", models.DateField()),
                ("imagen", models.FileField(blank=True, null=True, upload_to="")),
                ("frecuencia_envio", models.DateField()),
                ("id_campana", models.IntegerField()),
                ("estado", models.IntegerField()),
                ("titulo", models.CharField(max_length=20)),
                ("descripcion", models.CharField(max_length=100)),
                ("fecha_modificacion", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Publicidad",
            fields=[
                ("id_publicidad", models.AutoField(primary_key=True, serialize=False)),
                ("fecha_creacion", models.DateField()),
                ("estado", models.IntegerField()),
                ("imagen_publicitaria", models.FileField(upload_to="")),
                ("fecha_modificacion", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Publicista",
            fields=[
                ("id_publicista", models.AutoField(primary_key=True, serialize=False)),
                ("ruc", models.CharField(max_length=13)),
                ("nombre", models.CharField(max_length=30)),
                ("mail_contacto", models.CharField(max_length=40)),
                ("telefono", models.CharField(max_length=10)),
                ("fecha_creacion", models.DateField()),
                ("fecha_modificacion", models.DateField()),
                ("estado", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RolUsuario",
            fields=[
                ("id_rol_usuario", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=15)),
                ("estado", models.IntegerField()),
                ("fecha_registro", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="TallerBrandeo",
            fields=[
                ("id_taller", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=30)),
                ("direccion", models.CharField(max_length=70)),
                ("referencia", models.CharField(max_length=100)),
                ("telefono", models.CharField(max_length=10)),
                ("estado", models.IntegerField()),
                ("fecha_creacion", models.DateField()),
                ("fecha_modificacion", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Vehiculo",
            fields=[
                ("id_vehiculo", models.AutoField(primary_key=True, serialize=False)),
                ("telefono_conductor", models.IntegerField(blank=True, null=True)),
                ("placa", models.CharField(max_length=7)),
                ("anio", models.IntegerField()),
                ("categoria_vehiculo", models.IntegerField()),
                ("color_vehiculo", models.IntegerField()),
                ("imagen_izq", models.FileField(upload_to="")),
                ("imagen_der", models.FileField(upload_to="")),
                ("imagen_frontal", models.FileField(upload_to="")),
                ("imagen_trasera", models.FileField(upload_to="")),
                ("imagen_techo", models.FileField(upload_to="")),
                ("estado", models.IntegerField()),
                (
                    "id_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.cliente",
                    ),
                ),
                (
                    "id_marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.marcasvehiculos",
                    ),
                ),
                (
                    "id_modelo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.modelosvehiculos",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vista",
            fields=[
                ("id_vista", models.AutoField(primary_key=True, serialize=False)),
                ("estado", models.IntegerField()),
                ("nombre_vista", models.CharField(max_length=40)),
                ("descripcion", models.CharField(max_length=40)),
                (
                    "id_menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.menu",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VerificacionConductorCampana",
            fields=[
                (
                    "id_verificacion",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("cedula_conductor", models.IntegerField()),
                ("fecha_registro", models.DateField()),
                ("tipo_verificacion", models.CharField(max_length=20)),
                ("imagen_evidencia", models.FileField(upload_to="")),
                ("estado", models.IntegerField()),
                (
                    "id_campana",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.campanapublicitaria",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VehiculosAdmisiblesCampana",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "id_campana",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.campanapublicitaria",
                    ),
                ),
                (
                    "id_vehiculo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.vehiculo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("id_usuario", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.CharField(max_length=40)),
                ("placa", models.CharField(blank=True, max_length=8, null=True)),
                ("contrasena", models.CharField(max_length=10)),
                ("fecha_creacion", models.DateField()),
                ("fecha_modificacion", models.DateField()),
                ("estado", models.IntegerField()),
                (
                    "rol_usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.rolusuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TallerXEmpresa",
            fields=[
                ("id_taller", models.AutoField(primary_key=True, serialize=False)),
                ("estado", models.IntegerField()),
                ("fecha_creacion", models.DateField()),
                ("fecha_modificacion", models.DateField()),
                (
                    "id_empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.empresa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sector",
            fields=[
                ("id_sector", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=15)),
                ("fecha_creacion", models.DateField()),
                ("cerco_virtual", models.JSONField()),
                ("fecha_modificacion", models.DateField()),
                ("estado", models.IntegerField()),
                (
                    "id_empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.empresa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RecorridoRealizado",
            fields=[
                ("id_recorrido", models.AutoField(primary_key=True, serialize=False)),
                ("hora_inicio", models.DateTimeField()),
                ("fecha", models.DateField()),
                ("hora_fin", models.DateTimeField()),
                ("kilometraje_recorrido", models.IntegerField()),
                ("dinero_recaudado", models.FloatField()),
                ("estado", models.IntegerField()),
                (
                    "id_campana",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.campanapublicitaria",
                    ),
                ),
                (
                    "id_chofer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.chofer",
                    ),
                ),
                (
                    "id_vehiculo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.vehiculo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PermisosXRol",
            fields=[
                ("id_permisos", models.AutoField(primary_key=True, serialize=False)),
                ("id_rol", models.IntegerField()),
                ("id_menu", models.IntegerField()),
                ("id_vista", models.IntegerField()),
                ("estado", models.IntegerField()),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.menu",
                    ),
                ),
                (
                    "rol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.rolusuario",
                    ),
                ),
                (
                    "vista",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.vista",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Opciones",
            fields=[
                ("id_opcion", models.AutoField(primary_key=True, serialize=False)),
                ("nombre_vista", models.CharField(max_length=40)),
                ("descripcion", models.CharField(max_length=40)),
                ("estado", models.IntegerField()),
                (
                    "id_vista",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.vista",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MovimientoCapital",
            fields=[
                ("id_saldo", models.AutoField(primary_key=True, serialize=False)),
                ("tipo_transaccion", models.IntegerField()),
                ("descripcion", models.CharField(max_length=10)),
                ("fecha_transaccion", models.DateField()),
                ("monto_transaccion", models.FloatField()),
                ("saldo_acumulado", models.FloatField()),
                ("estado", models.IntegerField()),
                (
                    "id_campana",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.campanapublicitaria",
                    ),
                ),
                (
                    "id_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.cliente",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IngresoConductorCampana",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_registro", models.DateField()),
                ("estado", models.IntegerField()),
                (
                    "id_campana",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.campanapublicitaria",
                    ),
                ),
                (
                    "id_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.cliente",
                    ),
                ),
                (
                    "id_vehiculo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.vehiculo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FormularioRegistroCampana",
            fields=[
                ("id_formulario", models.AutoField(primary_key=True, serialize=False)),
                ("telefono_conductor", models.IntegerField()),
                ("licencia", models.FileField(upload_to="")),
                ("matricula", models.FileField(upload_to="")),
                ("numero_cuenta_bancaria", models.CharField(max_length=15)),
                ("cedula", models.CharField(max_length=10)),
                ("entidad_bancaria", models.IntegerField()),
                ("tipo_cuenta_bancaria", models.IntegerField()),
                ("correo_electronico", models.CharField(max_length=50)),
                ("fecha_envio", models.DateField()),
                (
                    "id_campana",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.campanapublicitaria",
                    ),
                ),
                (
                    "id_chofer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.chofer",
                    ),
                ),
                (
                    "id_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.cliente",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmpresaXPublicista",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("estado", models.IntegerField()),
                ("fecha_creacion", models.DateField()),
                ("fecha_modificacion", models.DateField()),
                (
                    "id_empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.empresa",
                    ),
                ),
                (
                    "id_publicista",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.publicista",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DetallePermisos",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("id_permisos", models.IntegerField()),
                ("id_opcion", models.IntegerField()),
                ("accion_permitida", models.BooleanField()),
                ("estado", models.IntegerField()),
                (
                    "opcion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.opciones",
                    ),
                ),
                (
                    "permisos",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_aplication.permisosxrol",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cliente",
            name="id_empresa",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="task_aplication.empresa",
            ),
        ),
        migrations.AddField(
            model_name="chofer",
            name="id_usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="task_aplication.usuario",
            ),
        ),
        migrations.AddField(
            model_name="campanapublicitaria",
            name="id_empresa",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="task_aplication.empresa",
            ),
        ),
    ]
