
#------------------------------------------------------
#  Sección de importación de módulos
#------------------------------------------------------
from django.contrib import admin
from .models import Letra, Origen, Palabra, Refran

#------------------------------------------------------
#  Clases para Letra
#------------------------------------------------------
class PalabrasInline(admin.TabularInline):
   model = Palabra
   extra = 0
   list_display = ['palabra','significado']
   fields = ['palabra']

class LetraAdmin(admin.ModelAdmin):
   list_display = ['letra']
   fields = ['letra']
   inlines = [PalabrasInline]

admin.site.register(Letra,LetraAdmin)

#------------------------------------------------------
#  Clases para Origen
#------------------------------------------------------
class PalabrasOrigenInline(admin.TabularInline):
   model = Palabra
   extra = 0
   list_display = ['palabra', 'significado']
   fields = ['palabra']

class RefranesOrigenInline(admin.TabularInline):
   model = Refran
   extra = 0
   list_display = ['dicho', 'explicacion']
   fields = ['dicho', 'explicacion']

class OrigenAdmin(admin.ModelAdmin):
   list_display = ['nombre', 'fecha', 'estado']
   fields = ['nombre', 'fecha', 'estado']
#   inlines = (PalabrasOrigenInline, RefranesOrigenInline)
   inlines = [RefranesOrigenInline]

admin.site.register(Origen,OrigenAdmin)

#------------------------------------------------------
#  Clases para Palabra
#------------------------------------------------------
class RefranesPalabraInline(admin.TabularInline):
   model = Refran
   extra = 0
   list_display = ['dicho', 'explicacion']
   fields = ['dicho', 'explicacion']

class PalabraAdmin(admin.ModelAdmin):
   list_display = ('palabra', 'significado', 'creador', 'fecha', 'estado')
#   list_filter = ('letra', 'fecha', 'estado')
   list_filter = ('letra', 'fecha', 'estado', 'origen')
#   fields = ['palabra', 'significado', 'fecha', ('letra', 'origen')]
   fieldsets = (
      (None, {'fields': ('palabra', 'significado')}),
      ('Detalle', {'fields': ('estado',('fecha', 'creador'),('letra','origen'))}),
   ) 
#   inlines = [RefranesPalabraInline]

admin.site.register(Palabra,PalabraAdmin)

#------------------------------------------------------
#  Clases para Refrán
#------------------------------------------------------
class RefranAdmin(admin.ModelAdmin):
   list_display = ('dicho', 'estado', 'fecha', 'creador')
#   list_filter = ('estado', 'fecha')
   list_filter = ('estado', 'fecha', 'estado', 'origen')
#   fields = ('estado', 'palabra', 'fecha')
#   fields = ['dicho', 'explicacion', ('palabra', 'fecha'), ('letra', 'origen')]
   fieldsets = (
      (None, {'fields': (('dicho', 'explicacion'),('creador', 'estado'))}),
      ('Detalle', {'fields': (('palabra','fecha') ,('letra','origen'),('fechaaprobacion','fechapublicacion'))}),
   )

admin.site.register(Refran,RefranAdmin)

#------------------------------------------------------
#  Fin de clases de administración
#------------------------------------------------------
