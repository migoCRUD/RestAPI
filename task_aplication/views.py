from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import EmailSerializer
from django.conf import settings
from django.template.loader import render_to_string



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
MenuSerializer, VistaSerializer, OpcionesSerializer,SectoresSerializer,EmpresasSerializer)

# Vistas para cada modelo

class SendEmailView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)

        if serializer.is_valid():
            message = serializer.validated_data['message']
            subject = serializer.validated_data['subject']
            from_email = settings.EMAIL_HOST_USER
            recipient_list = serializer.validated_data['recipient_list']

            #code = str(rd.randint(111111, 999999))
            #message = "El código para recuperar su contraseña es "+code
            #subject = "Migo Ads - Recuperación de contraseña"

            context = {
                'name': subject,
                'code': message
            }

            # Render the HTML template
            html_content = render_to_string('correo.html', context)

            email = EmailMessage("Migo Ads - Recuperación de contraseña", html_content, from_email, recipient_list)
            email.content_subtype = "html"
            email.send()

            return Response({'message': 'Email sent successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class SectoresPorUsuarioView(APIView):
    def get(self, request, usuario_id):
        try:
            # Obtener el rol del usuario
            usuario = Usuario.objects.get(id_usuario=usuario_id)
            id_rol = usuario.rol_usuario.id_rol_usuario

            # Obtener sectores para un usuario específico
            if id_rol == 1:  # 1 para administrador
                sectores = Sector.objects.all().distinct()
            elif id_rol == 2:  # 2 para publicista
                publicista = Publicista.objects.get(id_usuario=usuario)
                empresas_asociadas = EmpresaXPublicista.objects.filter(
                    id_publicista=publicista
                ).values_list("id_empresa", flat=True)
                sectores = Sector.objects.filter(id_empresa__in=empresas_asociadas).distinct()
            elif id_rol == 3:  # 3 para empresa
                empresa = Empresa.objects.get(id_usuario=usuario)
                sectores = Sector.objects.filter(id_empresa=empresa).distinct()
            else:
                return Response({"error": "Tipo de usuario no válido"}, status=status.HTTP_400_BAD_REQUEST)

            #serialización
            serializer = SectoresSerializer(sectores, many=True)

            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmpresasListView(APIView):
    def get(self, request, usuario_id):
        try:
            # Obtener el rol del usuario
            usuario = Usuario.objects.get(id_usuario=usuario_id)
            id_rol = usuario.rol_usuario.id_rol_usuario

            # Obtener la lista de empresas según el tipo de usuario
            if id_rol == 1:  # Administrador
                empresas = Empresa.objects.filter(id_usuario_administrador=usuario_id)
            elif id_rol == 2:  # Publicista
                publicista = Publicista.objects.get(id_usuario=usuario)
                empresas_asociadas = EmpresaXPublicista.objects.filter(
                    id_publicista=publicista
                ).values_list("id_empresa", flat=True)
                empresas = Empresa.objects.filter(id_empresa__in=empresas_asociadas)
            else:
                return Response({"error": "Tipo de usuario no válido"}, status=status.HTTP_400_BAD_REQUEST)

            #serialización
            serializer = EmpresasSerializer(empresas, many=True)

            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)