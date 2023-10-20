import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RestAPI.settings')
django.setup()

import random
from datetime import date, timedelta
from faker import Faker
from django.core.management.base import BaseCommand
from task_aplication.models import (RolUsuario, Usuario, Publicista, Empresa, Chofer, CampanaPublicitaria, Sector,
                            VehiculosAdmisiblesCampana, Vehiculo, ModelosVehiculos, MarcasVehiculos,
                            TallerXEmpresa, TallerBrandeo, Cliente)

class Command(BaseCommand):
    help = 'Load fake data into the database'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Roles de Usuario
        roles = ["Rol 1", "Rol 2", "Rol 3", "Rol 4", "Rol 5"]
        for role_name in roles:
            RolUsuario.objects.create(nombre=role_name, estado=random.choice([0, 1]), fecha_registro=date.today())

        # Usuarios
        roles = RolUsuario.objects.all()
        for _ in range(8):
            Usuario.objects.create(
                rol_usuario=random.choice(roles),
                email=fake.email(),
                contrasena=fake.password(length=10),
                fecha_creacion=date.today(),
                fecha_modificacion=date.today(),
                estado=random.choice([0, 1])
            )

        # Empresas Publicistas
        for _ in range(8):
            publicista = Publicista.objects.create(
                ruc=fake.random_int(min=10000000000, max=99999999999),
                nombre=fake.company(),
                mail_contacto=fake.email(),
                telefono=fake.phone_number(),
                fecha_creacion=date.today(),
                fecha_modificacion=date.today(),
                estado=random.choice([0, 1])
            )

            # Empresas
            empresa = Empresa.objects.create(
                ruc=fake.random_int(min=10000000000, max=99999999999),
                nombre=fake.company(),
                descripcion=fake.catch_phrase(),
                mail_contacto=fake.email(),
                telefono=fake.phone_number(),
                fecha_creacion=date.today(),
                fecha_modificacion=date.today(),
                estado=random.choice([0, 1])
            )

            # Relación EmpresaXPublicista
            EmpresaXPublicista.objects.create(
                id_publicista=publicista,
                id_empresa=empresa,
                estado=random.choice([0, 1]),
                fecha_creacion=date.today(),
                fecha_modificacion=date.today()
            )

        # Choferes
        usuarios = Usuario.objects.all()
        for _ in range(8):
            Chofer.objects.create(
                id_usuario=random.choice(usuarios),
                cedula_chofer=fake.random_int(min=1000000000, max=9999999999),
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=60),
                sexo=random.choice([1, 2]),  # Assuming 1 is male and 2 is female
                estado=random.choice([0, 1])
            )

        # Campañas Publicitarias
        empresas = Empresa.objects.all()
        for _ in range(8):
            campana = CampanaPublicitaria.objects.create(
                id_empresa=random.choice(empresas),
                nombre_campana=fake.company_suffix(),
                fecha_inicio=date.today(),
                fecha_fin=date.today() + timedelta(days=random.randint(1, 30)),
                fecha_fin_registro=date.today(),
                presupuesto=random.uniform(1000, 10000),
                nombre_responsable=fake.name(),
                tarifa_base=random.uniform(10, 100),
                taller_brandeo=fake.company_suffix(),
                carroceria_capo=fake.boolean(),
                puerta_conductor=fake.boolean(),
                puerta_pasajero=fake.boolean(),
                puerta_traseratzq=fake.boolean(),
                puerta_traseraDer=fake.boolean(),
                carroceria_guantera=fake.boolean(),
                carroceria_techo=fake.boolean(),
                fecha_creacion=date.today(),
                fecha_modificacion=date.today(),
                estado=random.choice([0, 1])
            )

            # Sectores
            for _ in range(4):
                Sector.objects.create(
                    id_empresa=random.choice(empresas),
                    nombre=fake.word(),
                    fecha_creacion=date.today(),
                    fecha_modificacion=date.today(),
                    estado=random.choice([0, 1])
                )

            # Vehículos Admisibles para la Campaña
            vehiculos = Vehiculo.objects.all()
            for _ in range(4):
                VehiculosAdmisiblesCampana.objects.create(
                    id_vehiculo=random.choice(vehiculos),
                    id_campana=campana
                )



        # Marcas de Vehículos
        for _ in range(5):
            MarcasVehiculos.objects.create(
                nombre=fake.word()
            )

        # Modelos de Vehículos
        marcas = MarcasVehiculos.objects.all()
        for _ in range(5):
            ModelosVehiculos.objects.create(
                id_marca=random.choice(marcas),
                nombre=fake.word()
            )

        # Vehículos
        clientes = Cliente.objects.all()
        modelos = ModelosVehiculos.objects.all()
        for _ in range(8):
            Vehiculo.objects.create(
                id_cliente=random.choice(clientes),
                telefono_conductor=fake.random_int(min=1000000000, max=9999999999),
                placa=fake.license_plate(),
                id_marca=random.choice(marcas),
                id_modelo=random.choice(modelos),
                anio=fake.year(),
                categoria_vehiculo=fake.random_int(min=1, max=5),
                color_vehiculo=fake.random_int(min=1, max=5),
                imagen_izq=None,  # Debes proporcionar las rutas de las imágenes
                imagen_der=None,
                imagen_frontal=None,
                imagen_trasera=None,
                imagen_techo=None,
                estado=random.choice([0, 1])
            )

        # TallerXEmpresa
        talleres = TallerBrandeo.objects.all()
        for _ in range(4):
            TallerXEmpresa.objects.create(
                id_taller=random.choice(talleres),
                id_empresa=random.choice(empresas),
                estado=random.choice([0, 1]),
                fecha_creacion=date.today(),
                fecha_modificacion=date.today()
            )

        # Taller de Brandeo
        for _ in range(4):
            TallerBrandeo.objects.create(
                nombre=fake.company(),
                direccion=fake.address(),
                referencia=fake.sentence(),
                telefono=fake.phone_number(),
                estado=random.choice([0, 1]),
                fecha_creacion=date.today(),
                fecha_modificacion=date.today()
            )

        # Clientes
        empresas = Empresa.objects.all()
        for _ in range(8):
            Cliente.objects.create(
                cedula_cliente=fake.random_int(min=1000000000, max=9999999999),
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=60),
                email=fake.email(),
                sexo=random.choice([1, 2]),  # Assuming 1 is male and 2 is female
                telefono=fake.phone_number(),
                id_empresa=random.choice(empresas),
                estado=random.choice([0, 1])
            )

        self.stdout.write(self.style.SUCCESS('Fake data has been loaded successfully.'))
