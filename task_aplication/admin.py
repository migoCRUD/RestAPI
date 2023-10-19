from django.contrib import admin
from .models import (
    Usuario, RolUsuario, DetallePermisos, PermisosXRol, Publicista, EmpresaXPublicista,
    Empresa, Sector, Notificacion, Publicidad, Chofer, RecorridoRealizado, MarcasVehiculos,
    ModelosVehiculos, Vehiculo, Cliente, VerificacionConductorCampana, MovimientoCapital,
    IngresoConductorCampana, FormularioRegistroCampana, CampanaPublicitaria,
    VehiculosAdmisiblesCampana, TallerXEmpresa, TallerBrandeo, Menu, Vista, Opciones)



# Register your models here.
admin.site.register(Usuario)
admin.site.register(RolUsuario)
admin.site.register(DetallePermisos)
admin.site.register(PermisosXRol)
admin.site.register(Publicista)
admin.site.register(EmpresaXPublicista)
admin.site.register(Empresa)
admin.site.register(Sector)
admin.site.register(Notificacion)
admin.site.register(Publicidad)
admin.site.register(Chofer)
admin.site.register(RecorridoRealizado)
admin.site.register(MarcasVehiculos)
admin.site.register(ModelosVehiculos)
admin.site.register(Vehiculo)
admin.site.register(Cliente)
admin.site.register(VerificacionConductorCampana)
admin.site.register(MovimientoCapital)
admin.site.register(IngresoConductorCampana)
admin.site.register(FormularioRegistroCampana)
admin.site.register(CampanaPublicitaria)
admin.site.register(VehiculosAdmisiblesCampana)
admin.site.register(TallerXEmpresa)
admin.site.register(TallerBrandeo)
admin.site.register(Menu)
admin.site.register(Vista)
admin.site.register(Opciones)