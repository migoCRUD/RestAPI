from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import (Usuario, RolUsuario, DetallePermisos, PermisosXRol, Publicista, EmpresaXPublicista,
Empresa, Sector, Notificacion, Publicidad, Chofer, RecorridoRealizado, MarcasVehiculos,
ModelosVehiculos, Vehiculo, Cliente, VerificacionConductorCampana, MovimientoCapital,
IngresoConductorCampana, FormularioRegistroCampana, CampanaPublicitaria,
VehiculosAdmisiblesCampana, TallerXEmpresa, TallerBrandeo, Menu, Vista, Opciones)

from .serializer import (UsuarioSerializer, RolUsuarioSerializer, DetallePermisosSerializer,
PermisosXRolSerializer, PublicistaSerializer, EmpresaXPublicistaSerializer, EmpresaSerializer,
SectorSerializer, NotificacionSerializer, PublicidadSerializer, ChoferSerializer,
RecorridoRealizadoSerializer, MarcasVehiculosSerializer, ModelosVehiculosSerializer,
VehiculoSerializer, ClienteSerializer, VerificacionConductorCampanaSerializer,
MovimientoCapitalSerializer, IngresoConductorCampanaSerializer,
FormularioRegistroCampanaSerializer, CampanaPublicitariaSerializer,
VehiculosAdmisiblesCampanaSerializer, TallerXEmpresaSerializer, TallerBrandeoSerializer,
MenuSerializer, VistaSerializer, OpcionesSerializer)

# Vistas para cada modelo

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RolUsuarioViewSet(viewsets.ModelViewSet):
    queryset = RolUsuario.objects.all()
    serializer_class = RolUsuarioSerializer

class DetallePermisosViewSet(viewsets.ModelViewSet):
    queryset = DetallePermisos.objects.all()
    serializer_class = DetallePermisosSerializer

class PermisosXRolViewSet(viewsets.ModelViewSet):
    queryset = PermisosXRol.objects.all()
    serializer_class = PermisosXRolSerializer

class PublicistaViewSet(viewsets.ModelViewSet):
    queryset = Publicista.objects.all()
    serializer_class = PublicistaSerializer

class EmpresaXPublicistaViewSet(viewsets.ModelViewSet):
    queryset = EmpresaXPublicista.objects.all()
    serializer_class = EmpresaXPublicistaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

class PublicidadViewSet(viewsets.ModelViewSet):
    queryset = Publicidad.objects.all()
    serializer_class = PublicidadSerializer

class ChoferViewSet(viewsets.ModelViewSet):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer

class RecorridoRealizadoViewSet(viewsets.ModelViewSet):
    queryset = RecorridoRealizado.objects.all()
    serializer_class = RecorridoRealizadoSerializer

class MarcasVehiculosViewSet(viewsets.ModelViewSet):
    queryset = MarcasVehiculos.objects.all()
    serializer_class = MarcasVehiculosSerializer

class ModelosVehiculosViewSet(viewsets.ModelViewSet):
    queryset = ModelosVehiculos.objects.all()
    serializer_class = ModelosVehiculosSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VerificacionConductorCampanaViewSet(viewsets.ModelViewSet):
    queryset = VerificacionConductorCampana.objects.all()
    serializer_class = VerificacionConductorCampanaSerializer

class MovimientoCapitalViewSet(viewsets.ModelViewSet):
    queryset = MovimientoCapital.objects.all()
    serializer_class = MovimientoCapitalSerializer

class IngresoConductorCampanaViewSet(viewsets.ModelViewSet):
    queryset = IngresoConductorCampana.objects.all()
    serializer_class = IngresoConductorCampanaSerializer

class FormularioRegistroCampanaViewSet(viewsets.ModelViewSet):
    queryset = FormularioRegistroCampana.objects.all()
    serializer_class = FormularioRegistroCampanaSerializer

class CampaniaPublicitariaViewSet(viewsets.ModelViewSet):
    queryset = CampanaPublicitaria.objects.all()
    serializer_class = CampanaPublicitariaSerializer

class VehiculosAdmisiblesCampanaViewSet(viewsets.ModelViewSet):
    queryset = VehiculosAdmisiblesCampana.objects.all()
    serializer_class = VehiculosAdmisiblesCampanaSerializer

class TallerXEmpresaViewSet(viewsets.ModelViewSet):
    queryset = TallerXEmpresa.objects.all()
    serializer_class = TallerXEmpresaSerializer

class TallerBrandeoViewSet(viewsets.ModelViewSet):
    queryset = TallerBrandeo.objects.all()
    serializer_class = TallerBrandeoSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class VistaViewSet(viewsets.ModelViewSet):
    queryset = Vista.objects.all()
    serializer_class = VistaSerializer

class OpcionesViewSet(viewsets.ModelViewSet):
    queryset = Opciones.objects.all()
    serializer_class = OpcionesSerializer