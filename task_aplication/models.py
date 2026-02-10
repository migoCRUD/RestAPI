from django.db import models
import hashlib

MEDIA_URL = 'media/'
EVIDENCE_URL = 'evidences/'
DOCS_URL = 'documents/'
ADS_URL = 'ads/'
NOTIF_URL = 'notifications/'
LOGOS_URL = 'empresas/logos/'
BANNERS_URL = 'empresas/banners/'

# Create your models here.

class Estado(models.Model):
    id_estado = models.IntegerField(default=0)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    ubicacion_google_maps = models.JSONField(default=dict)

    def __str__(self):
        return self.nombre

class EntidadBancaria(models.Model):
    id_entidad = models.AutoField(primary_key=True)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class RolUsuario(models.Model):
    id_rol_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    estado = models.IntegerField()
    fecha_registro = models.DateField()

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rol_usuario = models.ForeignKey(RolUsuario, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    placa = models.CharField(max_length=8, null=True, blank=True)
    contrasena = models.CharField(max_length=64)  # Longitud suficiente para almacenar el hash
    token_notificacion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    estado = models.IntegerField(choices=[(0, 'Inactivo'), (1, 'Activo'), (3, 'deshabilitado')], default=0)

    def save(self, *args, **kwargs):
        # Almacena la contraseña como un hash SHA-256 solo si se está creando un nuevo objeto
        if not self.id_usuario:
            self.contrasena = self._hash_password(self.contrasena)
        super().save(*args, **kwargs)

    def _hash_password(self, password):
        # Utiliza hashlib para calcular el hash SHA-256 de la contraseña
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        return sha256.hexdigest()

    def __str__(self):
        return self.email



class DetallePermisos(models.Model):
    id = models.AutoField(primary_key=True)
    id_permisos = models.IntegerField()
    id_opcion = models.IntegerField()
    accion_permitida = models.BooleanField()
    permisos = models.ForeignKey('PermisosXRol', on_delete=models.CASCADE)
    opcion = models.ForeignKey('Opciones', on_delete=models.CASCADE)
    estado = models.IntegerField()

    def __str__(self):
        return f"Detalle de Permisos #{self.id}"

class PermisosXRol(models.Model):
    id_permisos = models.AutoField(primary_key=True)
    id_rol = models.IntegerField()
    id_menu = models.IntegerField()
    id_vista = models.IntegerField()
    estado = models.IntegerField()
    rol = models.ForeignKey('RolUsuario', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    vista = models.ForeignKey('Vista', on_delete=models.CASCADE)

    def __str__(self):
        return f"Permisos de Rol #{self.id_permisos}"

class Publicista(models.Model):
    id_publicista = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=30)
    mail_contacto = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    estado = models.IntegerField()

    def __str__(self):
        return self.nombre

class EmpresaXPublicista(models.Model):
    id_publicista = models.ForeignKey('Publicista', on_delete=models.CASCADE)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    estado = models.IntegerField()
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()

    def __str__(self):
        return f"Empresa-Publicista #{self.id}"

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    mail_contacto = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class EmpresaImages(models.Model):
    id_images = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=LOGOS_URL, default="")
    banner = models.ImageField(upload_to=BANNERS_URL, default="")
    estado = models.IntegerField(default = 1)

    def __str__(self):
        return str(self.id_empresa)

class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    id_campana = models.ForeignKey('CampanaPublicitaria', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    cerco_virtual = models.JSONField()
    centro = models.JSONField(default=dict)
    zoom = models.IntegerField()
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    fecha_modificacion = models.DateField()
    estado = models.IntegerField()

    def __str__(self):
        return self.nombre

class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    fecha_envio = models.DateField()
    id_campana = models.IntegerField()
    ESTADO_NOTIFICACION = [
        ('leido', 'Leido'),
        ('no leido', 'No Leido'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_NOTIFICACION)
    titulo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Publicidad(models.Model):
    id_publicidad = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField()
    estado = models.IntegerField()
    imagen_publicitaria = models.FileField(upload_to=ADS_URL)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    fecha_modificacion = models.DateField()

    def __str__(self):
        return f"Publicidad #{self.id_publicidad}"

class Chofer(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_chofer = models.AutoField(primary_key=True)
    cedula_chofer = models.CharField(max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    sexo = models.IntegerField()
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    estado = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class RecorridoRealizado(models.Model):
    id_recorrido = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, default=1)
    id_campana = models.ForeignKey('CampanaPublicitaria', on_delete=models.CASCADE)
    id_vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    fecha_hora_inicio = models.CharField(max_length=50)
    fecha_hora_fin = models.CharField(max_length=50)
    kilometraje_recorrido = models.FloatField(default=0.0)
    dinero_recaudado = models.FloatField()
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    estado = models.IntegerField()
    ubicaciones = models.JSONField(default=list)

    def __str__(self):
        return f"Recorrido #{self.id_recorrido}"

class MarcasVehiculos(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    estado = models.CharField(default="Activo")

    def __str__(self):
        return self.nombre

class ModelosVehiculos(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    id_marca = models.ForeignKey('MarcasVehiculos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    estado = models.CharField(default="Activo")

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True, blank=True)
    id_chofer = models.ForeignKey('Chofer', on_delete=models.CASCADE, null=True, blank=True)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=True, blank=True)
    id_vehiculo = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=7)
    id_marca = models.ForeignKey('MarcasVehiculos', on_delete=models.CASCADE)
    id_modelo = models.ForeignKey('ModelosVehiculos', on_delete=models.CASCADE)
    anio = models.IntegerField()
    TIPOS_DE_AUTOS = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('camioneta', 'Camioneta'),
        ('camion', 'Camion'),
        ('bus', 'Bus'),
    ]
    categoria_vehiculo = models.CharField(max_length=20, choices=TIPOS_DE_AUTOS)
    color_vehiculo = models.CharField(max_length=20)
    imagen_izq = models.ImageField(upload_to=MEDIA_URL, default="")
    imagen_der = models.ImageField(upload_to=MEDIA_URL, default="")
    imagen_frontal = models.ImageField(upload_to=MEDIA_URL, default="")
    imagen_trasera = models.ImageField(upload_to=MEDIA_URL, default="")
    imagen_techo = models.ImageField(upload_to=MEDIA_URL, default="")
    estado = models.IntegerField()

    def __str__(self):
        return self.placa

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    cedula_cliente = models.CharField(max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    email = models.CharField(max_length=40)
    sexo = models.IntegerField()
    telefono = models.CharField(max_length=10)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)
    id_campana = models.ForeignKey('CampanaPublicitaria', on_delete=models.CASCADE, null=True, blank=True)
    estado = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class VerificacionConductorCampana(models.Model):
    id_verificacion = models.AutoField(primary_key=True)
    cedula_conductor = models.IntegerField()
    id_campana = models.ForeignKey('CampanaPublicitaria', on_delete=models.CASCADE)
    fecha_registro = models.DateField()
    tipo_verificacion = models.CharField(max_length=20)
    imagen_evidencia = models.ImageField(upload_to=MEDIA_URL, default="")
    estado = models.IntegerField()

    def __str__(self):
        return f"Verificación #{self.id_verificacion}"

class MovimientoCapital(models.Model):
    id_saldo = models.AutoField(primary_key=True)
    id_campana = models.ForeignKey('CampanaPublicitaria', on_delete=models.CASCADE)
    tipo_transaccion = models.IntegerField()
    descripcion = models.CharField(max_length=10)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha_transaccion = models.DateField()
    monto_transaccion = models.FloatField()
    saldo_acumulado = models.FloatField()
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    estado = models.IntegerField()

    def __str__(self):
        return f"Transacción de Capital #{self.id_saldo}"

class IngresoConductorCampana(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, default=1)
    id_campana = models.ForeignKey('CampanaPublicitaria', on_delete=models.CASCADE)
    id_formulario_registro = models.IntegerField(default=1)
    fecha_registro = models.DateField()
    id_vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    estado = models.IntegerField()
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    documento_QR = models.FileField(upload_to=DOCS_URL, default="")
    imagen_QR = models.ImageField(upload_to=MEDIA_URL, default="")

    def __str__(self):
        return f"Ingreso Conductor-Campaña #{self.id_usuario}"

class FormularioRegistroCampana(models.Model):
    id_formulario = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, default=1)
    id_campana = models.ForeignKey('CampanaPublicitaria', on_delete=models.CASCADE)
    telefono_conductor = models.IntegerField()
    licencia = models.FileField(upload_to=DOCS_URL)
    matricula = models.FileField(upload_to=DOCS_URL)
    numero_cuenta_bancaria = models.CharField(max_length=15)
    cedula = models.CharField(max_length=10)
    entidad_bancaria = models.CharField()
    tipo_cuenta_bancaria = models.CharField()
    correo_electronico = models.CharField(max_length=50)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    id_vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, default=4)
    fecha_envio = models.DateField()
    estado_solicitud = models.CharField(default="pendiente")
    brandeo = models.BooleanField(default=False)
    carroceria_capo = models.BooleanField(default=False)
    carroceria_techo = models.BooleanField(default=False)
    puerta_conductor = models.BooleanField(default=False)
    puerta_pasajero = models.BooleanField(default=False)
    puerta_trasera_iz = models.BooleanField(default=False)
    puerta_trasera_der = models.BooleanField(default=False)
    puerta_maletero = models.BooleanField(default=False)

    def __str__(self):
        return f"Formulario Registro-Campaña #{self.id_formulario}"

class CampanaPublicitaria(models.Model):
    id_campana = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    nombre_campana = models.CharField(max_length=20)
    correo_responsable = models.CharField(max_length=40)
    id_sector = models.IntegerField(null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_fin_registro = models.DateField()
    presupuesto = models.FloatField()
    nombre_responsable = models.CharField(max_length=20)
    tarifa_base = models.FloatField()
    tarifa_min = models.FloatField()
    tarifa_max = models.FloatField()
    hora_monetizable_inicio = models.CharField(max_length=5)
    hora_monetizable_fin = models.CharField(max_length=5)
    cobro_minimo = models.FloatField()
    TIPOS_BRANDEOS = [
        ('sticker', 'Sticker'),
        ('panel led', 'Panel LED'),
    ]
    tipo_brandeo = models.CharField(max_length=20, choices=TIPOS_BRANDEOS)
    id_talleres = models.JSONField(default=list)
    carroceria_capo = models.FloatField(default=0.0)
    carroceria_techo = models.FloatField(default=0.0)
    puerta_conductor = models.FloatField(default=0.0)
    puerta_pasajero = models.FloatField(default=0.0)
    puerta_trasera_iz = models.FloatField(default=0.0)
    puerta_trasera_der = models.FloatField(default=0.0)
    puerta_maletero = models.FloatField(default=0.0)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()
    estado = models.IntegerField()
    sedan_admisible = models.BooleanField()
    suv_admisible = models.BooleanField()
    camion_admisible = models.BooleanField()
    camioneta_admisible = models.BooleanField()
    bus_admisible = models.BooleanField()

    def __str__(self):
        return self.nombre_campana

class VehiculosAdmisiblesCampana(models.Model):
    id_vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    id_campana = models.ForeignKey('CampanaPublicitaria', on_delete=models.CASCADE)


class TallerXEmpresa(models.Model):
    id_taller = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    estado = models.IntegerField()
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()

    def __str__(self):
        return f"Taller-Empresa #{self.id_taller}"

class TallerBrandeo(models.Model):
    id_taller = models.AutoField(primary_key=True)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    referencia = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    estado = models.IntegerField()
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()

    def __str__(self):
        return self.nombre

class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    estado = models.IntegerField()
    nombre_menu = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre_menu

class Vista(models.Model):
    id_vista = models.AutoField(primary_key=True)
    id_menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    estado = models.IntegerField()
    nombre_vista = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre_vista

class Opciones(models.Model):
    id_opcion = models.AutoField(primary_key=True)
    id_vista = models.ForeignKey('Vista', on_delete=models.CASCADE)
    nombre_vista = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    estado = models.IntegerField()

    def __str__(self):
        return self.nombre_vista
