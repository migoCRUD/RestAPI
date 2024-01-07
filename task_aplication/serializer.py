from rest_framework import serializers
#from rest_framework_simplejwt.tokens import RefreshToken
#from django.contrib.auth.hashers import check_password
from .models import (Usuario, RolUsuario, DetallePermisos, PermisosXRol, Publicista, EmpresaXPublicista,
Empresa, Sector, Notificacion, Publicidad, Chofer, RecorridoRealizado, MarcasVehiculos,
ModelosVehiculos, Vehiculo, Cliente, VerificacionConductorCampana, MovimientoCapital,
IngresoConductorCampana, FormularioRegistroCampana, CampanaPublicitaria,
VehiculosAdmisiblesCampana, TallerXEmpresa, TallerBrandeo, Menu, Vista, Opciones)


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    #from_email = serializers.EmailField()
    recipient_list = serializers.ListField(child=serializers.EmailField())

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class RolUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolUsuario
        fields = '__all__'

class DetallePermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePermisos
        fields = '__all__'

class PermisosXRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisosXRol
        fields = '__all__'

class PublicistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicista
        fields = '__all__'

class EmpresaXPublicistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaXPublicista
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

class PublicidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicidad
        fields = '__all__'

class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = '__all__'

class RecorridoRealizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecorridoRealizado
        fields = '__all__'

class MarcasVehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcasVehiculos
        fields = '__all__'

class ModelosVehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelosVehiculos
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VerificacionConductorCampanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificacionConductorCampana
        fields = '__all__'

class MovimientoCapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoCapital
        fields = '__all__'

class IngresoConductorCampanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngresoConductorCampana
        fields = '__all__'

class FormularioRegistroCampanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormularioRegistroCampana
        fields = '__all__'

class CampanaPublicitariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampanaPublicitaria
        fields = '__all__'

class VehiculosAdmisiblesCampanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculosAdmisiblesCampana
        fields = '__all__'

class TallerXEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TallerXEmpresa
        fields = '__all__'

class TallerBrandeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TallerBrandeo
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class VistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vista
        fields = '__all__'

class OpcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opciones
        fields = '__all__'

class SectoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class EmpresasSerializer(serializers.Serializer):
    class Meta:
        model = Empresa
        fields = ['id_empresa', 'nombre_empresa']