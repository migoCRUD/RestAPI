from django.urls import path , include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from task_aplication import views


router = routers.DefaultRouter()
#router.register(r"Usuarios",views.aplicationView,'Usuario')

# Registra las vistas para los modelos en el enrutador
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'rolusuarios', views.RolUsuarioViewSet)
router.register(r'detallepermisos', views.DetallePermisosViewSet)
router.register(r'permisosxrol', views.PermisosXRolViewSet)
router.register(r'publicistas', views.PublicistaViewSet)
router.register(r'empresaxpublicistas', views.EmpresaXPublicistaViewSet)
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'sectores', views.SectorViewSet)
router.register(r'notificaciones', views.NotificacionViewSet)
router.register(r'publicidades', views.PublicidadViewSet)
router.register(r'choferes', views.ChoferViewSet)
router.register(r'recorridosrealizados', views.RecorridoRealizadoViewSet)
router.register(r'marcasvehiculos', views.MarcasVehiculosViewSet)
router.register(r'modelosvehiculos', views.ModelosVehiculosViewSet)
router.register(r'vehiculos', views.VehiculoViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'verificacionesconductorcampana', views.VerificacionConductorCampanaViewSet)
router.register(r'movimientocapital', views.MovimientoCapitalViewSet)
router.register(r'ingresoconductorcampana', views.IngresoConductorCampanaViewSet)
router.register(r'formularioregistrocampana', views.FormularioRegistroCampanaViewSet)
router.register(r'campaniaspublicitarias', views.CampaniaPublicitariaViewSet)
router.register(r'vehiculosadmisiblescampana', views.VehiculosAdmisiblesCampanaViewSet)
router.register(r'tallerxempresas', views.TallerXEmpresaViewSet)
router.register(r'tallerbrandeos', views.TallerBrandeoViewSet)
router.register(r'menus', views.MenuViewSet)
router.register(r'vistas', views.VistaViewSet)
router.register(r'opciones', views.OpcionesViewSet)

# Define las rutas
urlpatterns=[
    path("Database/", include(router.urls)),
    path('documents/', include_docs_urls(title='Aplication API')),
    path('send_email/<str:subject>/<str:message>/<str:from_email>/<str:recipient_list>/', views.SendEmailView.as_view(), name='send_email')
    ]
# se genera el CRUD