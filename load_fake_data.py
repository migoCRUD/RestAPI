import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RestAPI.settings")  
django.setup()

from task_aplication.models import Usuario, RolUsuario, DetallePermisos, PermisosXRol, Publicista, EmpresaXPublicista, Empresa, Sector, Notificacion, Publicidad, Chofer, RecorridoRealizado, MarcasVehiculos, ModelosVehiculos, Vehiculo, Cliente, VerificacionConductorCampana, MovimientoCapital, IngresoConductorCampana, FormularioRegistroCampana, CampaniaPublicitaria, VehiculosAdmisiblesCampana, TallerXEmpresa, TallerBrandeo, Menu, Vista, Opciones

fake = Faker()


# Tabla Usuario
for i in range(1, 11):
    Usuario.objects.create(
        estado=i % 2,
        email=f"usuario{i}@ejemplo.com",
        placa=f"ABC12{i}",
        contrasena=f"password{i}",
        fecha_creacion=f"2023-10-{10 + i}",
        fecha_modificacion=f"2023-10-{20 + i}",
        rol_usuario=i
    )

# Tabla RolUsuario
for i in range(1, 11):
    RolUsuario.objects.create(
        nombre=f"Rol de Prueba {i}",
        estado=i % 2,
        fecha_registro=f"2023-10-{10 + i}"
    )

# Tabla DetallePermisos
for i in range(1, 11):
    DetallePermisos.objects.create(
        id_permisos=i,
        id_opcion=i,
        accion_permitida=i % 2 == 0,
        estado=i % 2,
        permisos_id=i % 5 + 1,
        opcion_id=i % 5 + 1
    )

# Tabla PermisosXRol
for i in range(1, 11):
    PermisosXRol.objects.create(
        id_rol=i,
        id_menu=i,
        id_vista=i,
        estado=i % 2,
        rol_id=i % 5 + 1,
        menu_id=i % 5 + 1,
        vista_id=i % 5 + 1
    )

# Tabla Publicista
for i in range(1, 11):
    Publicista.objects.create(
        RUC=f"RUC{i}",
        nombre=f"Publicista {i}",
        mail_contacto=f"publicista{i}@ejemplo.com",
        telefono=f"1234567{i}",
        fecha_creacion=f"2023-10-{10 + i}",
        fecha_modificacion=f"2023-10-{20 + i}",
        estado=i % 2
    )

# Tabla EmpresaXPublicista
for i in range(1, 11):
    EmpresaXPublicista.objects.create(
        id_publicista_id=i,
        id_empresa_id=i,
        estado=i % 2,
        fecha_creacion=f"2023-10-{10 + i}",
        fecha_modificacion=f"2023-10-{20 + i}"
    )

# Tabla Empresa
for i in range(1, 11):
    Empresa.objects.create(
        RUC=f"RUC{i}",
        nombre=f"Empresa {i}",
        descripcion=f"Descripción Empresa {i}",
        mail_contacto=f"empresa{i}@ejemplo.com",
        telefono=f"1234567{i}",
        fecha_creacion=f"2023-10-{10 + i}",
        fecha_modificacion=f"2023-10-{20 + i}",
        estado=i % 2
    )

# Tabla Sector
for i in range(1, 11):
    Sector.objects.create(
        id_empresa_id=i,
        nombre=f"Sector {i}",
        fecha_creacion=f"2023-10-{10 + i}",
        cerco_virtual={f"latitud{i}", f"longitud{i}"},
        fecha_modificacion=f"2023-10-{20 + i}",
        estado=i % 2
    )

# Tabla Notificacion
for i in range(1, 11):
    Notificacion.objects.create(
        Fecha_creacion=f"2023-10-{10 + i}",
        Fecha_fin=f"2023-10-{20 + i}",
        imagen=None,
        frecuencia_envio=f"2023-10-{30 + i}",
        id_campana=i,
        estado=i % 2,
        titulo=f"Notificación {i}",
        descripcion=f"Descripción Notificación {i}",
        fecha_modificacion=f"2023-10-{40 + i}"
    )

# Tabla Publicidad
for i in range(1, 11):
    Publicidad.objects.create(
        fecha_creacion=f"2023-10-{10 + i}",
        estado=i % 2,
        imagen_publicitaria=None,
        fecha_modificacion=f"2023-10-{20 + i}"
    )

# Tabla Chofer
for i in range(1, 11):
    Chofer.objects.create(
        id_usuario_id=i,
        cedula_chofer=f"1234567{i}",
        nombre=f"Chofer Nombre {i}",
        apellido=f"Chofer Apellido {i}",
        fecha_nacimiento=f"1990-01-{10 + i}",
        sexo=i % 2
    )

# Tabla RecorridoRealizado
for i in range(1, 11):
    RecorridoRealizado.objects.create(
        id_chofer_id=i,
        id_campana_id=i,
        id_vehiculo_id=i,
        hora_inicio=f"2023-10-{10 + i}T08:00:00Z",
        fecha=f"2023-10-{20 + i}",
        hora_fin=f"2023-10-{20 + i}T18:00:00Z",
        kilometraje_recorrido=i * 100,
        dinero_recaudado=i * 1000.0
    )

# Tabla MarcasVehiculos
for i in range(1, 11):
    MarcasVehiculos.objects.create(
        nombre=f"Marca {i}"
    )

# Tabla ModelosVehiculos
for i in range(1, 11):
    ModelosVehiculos.objects.create(
        id_marca_id=i % 10 + 1,
        nombre=f"Modelo {i}"
    )

# Tabla Vehiculo
for i in range(1, 11):
    Vehiculo.objects.create(
        id_cliente_id=i % 10 + 1,
        telefono_conductor=None,
        placa=f"ABC12{i}",
        id_marca_id=i % 10 + 1,
        id_modelo_id=i % 10 + 1,
        año=2023,
        categoría_vehiculo=i % 5,
        color_vehiculo=i % 5,
        imagen_izq=None,
        imagen_der=None,
        imagen_frontal=None,
        imagen_trasera=None,
        imagen_techo=None
    )

# Tabla Cliente
for i in range(1, 11):
    Cliente.objects.create(
        cedula_cliente=f"1234567{i}",
        nombre=f"Cliente Nombre {i}",
        apellido=f"Cliente Apellido {i}",
        fecha_nacimiento=f"1990-01-{10 + i}",
        email=f"cliente{i}@ejemplo.com",
        sexo=i % 2,
        telefono=f"1234567{i}",
        id_empresa_id=i % 10 + 1,
        id_campaña_id=i % 10 + 1
    )

# Tabla VerificacionConductorCampana
for i in range(1, 11):
    VerificacionConductorCampana.objects.create(
        cedula_conductor=i * 1000,
        id_campana_id=i % 10 + 1,
        fecha_registro=f"2023-10-{10 + i}",
        tipo_verificacion=f"Verificación {i}",
        Imagen_evidencia=None
    )

# Tabla MovimientoCapital
for i in range(1, 11):
    MovimientoCapital.objects.create(
        id_campana_id=i % 10 + 1,
        tipo_transaccion=i % 5,
        descripcion=f"Transacción {i}",
        id_cliente_id=i % 10 + 1,
        fecha_transaccion=f"2023-10-{10 + i}",
        monto_transaccion=i * 1000.0,
        saldo_acumulado=i * 10000.0
    )

# Tabla IngresoConductorCampana
for i in range(1, 11):
    IngresoConductorCampana.objects.create(
        id_cliente_id=i % 10 + 1,
        Id_campana_id=i % 10 + 1,
        fecha_registro=f"2023-10-{10 + i}",
        id_vehiculo_id=i % 10 + 1,
        estado=i % 2
    )

# Tabla FormularioRegistroCampana
for i in range(1, 11):
    FormularioRegistroCampana.objects.create(
        id_chofer_id=i % 10 + 1,
        id_cliente_id=i % 10 + 1,
        id_campana_id=i % 10 + 1,
        teléfono_conductor=f"1234567{i}",
        licencia=None,
        matricula=None,
        numero_cuenta_bancaria=f"Cuenta{i}",
        cedula=f"1234567{i}",
        entidad_bancaria=i % 5,
        tipo_cuenta_bancaria=i % 5,
        correo_electronico=f"formulario{i}@ejemplo.com",
        fecha_envio=f"2023-10-{10 + i}"
    )

# Tabla CampaniaPublicitaria
for i in range(1, 11):
    CampaniaPublicitaria.objects.create(
        Id_empresa_id=i % 10 + 1,
        Nombre_campana=f"Campania {i}",
        Fecha_inicio=f"2023-10-{10 + i}",
        fecha_fin=f"2023-10-{20 + i}",
        fecha_fin_registro=f"2023-10-{30 + i}",
        presupuesto=i * 10000.0,
        nombre_responsable=f"Responsable {i}",
        tarifa_base=i * 100.0,
        taller_brandeo=f"Taller {i}",
        carrocería_capo=i % 2 == 0,
        puerta_conductor=i % 2 == 0,
        puerta_pasajero=i % 2 == 0,
        puerta_traseratzq=i % 2 == 0,
        puerta_traseraDer=i % 2 == 0,
        carrocería_guantera=i % 2 == 0,
        carroceria_techo=i % 2 == 0,
        fecha_creacion=f"2023-10-{10 + i}",
        fecha_modificacion=f"2023-10-{40 + i}"
    )

# Tabla VehiculosAdmisiblesCampana
for i in range(1, 11):
    VehiculosAdmisiblesCampana.objects.create(
        id_vehiculo_id=i % 10 + 1,
        id_campana_id=i % 10 + 1
    )

# Tabla TallerXEmpresa
for i in range(1, 11):
    TallerXEmpresa.objects.create(
        id_empresa_id=i % 10 + 1,
        estado=i % 2,
        fecha_creacion=f"2023-10-{10 + i}",
        fecha_modificacion=f"2023-10-{20 + i}"
    )

# Tabla TallerBrandeo
for i in range(1, 11):
    TallerBrandeo.objects.create(
        nombre=f"Taller de Brandeo {i}",
        direccion=f"Dirección Taller {i}",
        referencia=f"Referencia Taller {i}",
        telefono=f"1234567{i}",
        estado=i % 2,
        fecha_creacion=f"2023-10-{10 + i}",
        fecha_modificacion=f"2023-10-{20 + i}"
    )

# Tabla Menu
for i in range(1, 11):
    Menu.objects.create(
        estado=i % 2,
        nombre_menu=f"Menú {i}",
        descripcion=f"Descripción Menú {i}"
    )

# Tabla Vista
for i in range(1, 11):
    Vista.objects.create(
        id_menu_id=i % 10 + 1,
        estado=i % 2,
        nombre_vista=f"Vista {i}",
        descripcion=f"Descripción Vista {i}"
    )

# Tabla Opciones
for i in range(1, 11):
    Opciones.objects.create(
        id_vista_id=i % 10 + 1,
        nombre_vista=f"Opción {i}",
        descripcion=f"Descripción Opción {i}",
        estado=i % 2
    )
