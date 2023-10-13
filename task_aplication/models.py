from django.db import models

# Create your models here.
        
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rol_usuario = models.IntegerField()
    email = models.CharField(max_length=40)
    placa = models.CharField(max_length=8, null=True, blank=True)
    contrasena = models.CharField(max_length=10)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()
    estado = models.IntegerField()
    rol_usuario = models.ForeignKey('RolUsuario')
    

    def __str__(self):
        return self.nombre_usuario

class RolUsuario(models.Model):
    id_rol_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    estado = models.IntegerField()
    fecha_registro = models.DateField()

    def __str__(self):
        return self.nombre

class DetallePermisos(models.Model):
    id = models.AutoField(primary_key=True)
    id_permisos = models.IntegerField()
    id_opcion = models.IntegerField()
    accion_permitida = models.BooleanField()
    estado = models.IntegerField()
    id_permisos = models.ForeignKey('PermisosXRol', on_delete=models.CASCADE)
    id_opcion = models.ForeignKey('Opciones', on_delete=models.CASCADE)

    def __str__(self):
        return f"Detalle de Permisos #{self.id}"

class PermisosXRol(models.Model):
    id_permisos = models.AutoField(primary_key=True)
    id_rol = models.IntegerField()
    id_menu = models.IntegerField()
    id_vista = models.IntegerField()
    estado = models.IntegerField()
    id_rol = models.ForeignKey('RolUsuario')
    id_menu = models.ForeignKey('Menu')
    id_vista = models.ForeignKey('Vista')

    def __str__(self):
        return f"Permisos de Rol #{self.id_permisos}"

class Publicista(models.Model):
    id_publicista = models.AutoField(primary_key=True)
    RUC = models.CharField(max_length=13)
    nombre = models.CharField(max_length=30)
    mail_contacto = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()
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
    RUC = models.CharField(max_length=13)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    mail_contacto = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()
    estado = models.IntegerField()

    def __str__(self):
        return self.nombre

class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=15)
    fecha_creacion = models.DateField()
    cerco_virtual = models.JSONField()
    fecha_modificacion = models.DateField()
    estado = models.IntegerField()

    def __str__(self):
        return self.nombre

class Notificacion(models.Model):
    Id_notificacion = models.AutoField(primary_key=True)
    Fecha_creacion = models.DateField()
    Fecha_fin = models.DateField()
    imagen = models.FileField(null=True, blank=True)
    frecuencia_envio = models.DateField()
    id_campana = models.IntegerField()
    estado = models.IntegerField()
    titulo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    fecha_modificacion = models.DateField()

    def __str__(self):
        return self.titulo

class Publicidad(models.Model):
    id_publicidad = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField()
    estado = models.IntegerField()
    imagen_publicitaria = models.FileField()
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

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class RecorridoRealizado(models.Model):
    id_recorrido = models.AutoField(primary_key=True)
    id_chofer = models.ForeignKey('Chofer', on_delete=models.CASCADE)
    id_campana = models.ForeignKey('CampaniaPublicitaria', on_delete=models.CASCADE)
    id_vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField()
    fecha = models.DateField()
    hora_fin = models.DateTimeField()
    kilometraje_recorrido = models.IntegerField()
    dinero_recaudado = models.FloatField()

    def __str__(self):
        return f"Recorrido #{self.id_recorrido}"

class MarcasVehiculos(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class ModelosVehiculos(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    id_marca = models.ForeignKey('MarcasVehiculos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    id_vehiculo = models.AutoField(primary_key=True)
    telefono_conductor = models.IntegerField(null=True, blank=True)
    placa = models.CharField(max_length=7)
    id_marca = models.ForeignKey('MarcasVehiculos', on_delete=models.CASCADE)
    id_modelo = models.ForeignKey('ModelosVehiculos', on_delete=models.CASCADE)
    año = models.IntegerField()
    categoría_vehiculo = models.IntegerField()
    color_vehiculo = models.IntegerField()
    imagen_izq = models.FileField()
    imagen_der = models.FileField()
    imagen_frontal = models.FileField()
    imagen_trasera = models.FileField()
    imagen_techo = models.FileField()

    def __str__(self):
        return self.placa

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cedula_cliente = models.CharField(max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    email = models.CharField(max_length=40)
    sexo = models.IntegerField()
    telefono = models.CharField(max_length=10)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)
    id_campaña = models.ForeignKey('CampaniaPublicitaria', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class VerificacionConductorCampana(models.Model):
    cedula_conductor = models.IntegerField()
    id_campana = models.ForeignKey('CampaniaPublicitaria', on_delete=models.CASCADE)
    fecha_registro = models.DateField()
    tipo_verificacion = models.CharField(max_length=20)
    Imagen_evidencia = models.FileField()

    def __str__(self):
        return f"Verificación #{self.id}"

class MovimientoCapital(models.Model):
    Id_saldo = models.AutoField(primary_key=True)
    id_campana = models.ForeignKey('CampaniaPublicitaria', on_delete=models.CASCADE)
    tipo_transaccion = models.IntegerField()
    descripcion = models.CharField(max_length=10)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha_transaccion = models.DateField()
    monto_transaccion = models.FloatField()
    saldo_acumulado = models.FloatField()

    def __str__(self):
        return f"Transacción de Capital #{self.Id_saldo}"

class IngresoConductorCampana(models.Model):
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    Id_campana = models.ForeignKey('CampaniaPublicitaria', on_delete=models.CASCADE)
    fecha_registro = models.DateField()
    id_vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    estado = models.IntegerField()

    def __str__(self):
        return f"Ingreso Conductor-Campaña #{self.id_cliente}"

class FormularioRegistroCampana(models.Model):
    id_formulario = models.AutoField(primary_key=True)
    id_chofer = models.ForeignKey('Chofer', on_delete=models.CASCADE)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    id_campana = models.ForeignKey('CampaniaPublicitaria', on_delete=models.CASCADE)
    teléfono_conductor = models.IntegerField()
    licencia = models.FileField()
    matricula = models.FileField()
    numero_cuenta_bancaria = models.CharField(max_length=15)
    cedula = models.CharField(max_length=10)
    entidad_bancaria = models.IntegerField()
    tipo_cuenta_bancaria = models.IntegerField()
    correo_electronico = models.CharField(max_length=50)
    fecha_envio = models.DateField()

    def __str__(self):
        return f"Formulario Registro-Campaña #{self.id_formulario}"

class CampaniaPublicitaria(models.Model):
    Id_campaña = models.AutoField(primary_key=True)
    Id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    Nombre_campana = models.CharField(max_length=20)
    Fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_fin_registro = models.DateField()
    presupuesto = models.FloatField()
    nombre_responsable = models.CharField(max_length=20)
    tarifa_base = models.FloatField()
    taller_brandeo = models.CharField(max_length=20)
    carrocería_capo = models.BooleanField()
    puerta_conductor = models.BooleanField()
    puerta_pasajero = models.BooleanField()
    puerta_traseratzq = models.BooleanField()
    puerta_traseraDer = models.BooleanField()
    carrocería_guantera = models.BooleanField()
    carroceria_techo = models.BooleanField()
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()

    def __str__(self):
        return self.Nombre_campaña

class VehiculosAdmisiblesCampana(models.Model):
    id_vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    id_campana = models.ForeignKey('CampaniaPublicitaria', on_delete=models.CASCADE)


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
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=70)
    referencia = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
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
