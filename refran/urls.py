
#------------------------------------------------------
#  Sección de importación de módulos
#------------------------------------------------------
from . import views
from django.urls import path

#------------------------------------------------------
#  Paths generales de acceso a instancias
#------------------------------------------------------
urlpatterns = [
   path('', views.index, name='index'),
   path('letras/', views.LetraListView.as_view(), name='letras'),
   path('letras/<uuid:pk>', views.LetraDetailView.as_view(), name='letra-detalle'),
   path('origenes/', views.OrigenListView.as_view(), name='origenes'),
   path('origenes/<uuid:pk>', views.OrigenDetailView.as_view(), name='origen-detalle'),
   path('palabras/', views.PalabraListView.as_view(), name='palabras'),
   path('palabras/<uuid:pk>', views.PalabraDetailView.as_view(), name='palabra-detalle'),
   path('refranes/', views.RefranListView.as_view(), name='refranes'),
   path('refranes/<uuid:pk>', views.RefranDetailView.as_view(), name='refran-detalle'),
   path('notas', views.notas, name='notas'),
   ]

#------------------------------------------------------
#  Paths a instancias filtradas
#------------------------------------------------------
urlpatterns += [
   path('refenrevision/', views.RefenRevisionListView.as_view(), name='refranes-enrevision'),
   path('refaprobados/', views.RefAprobadosListView.as_view(), name='refranes-aprobados'),
   path('refpublicados/', views.RefPublicadosListView.as_view(), name='refranes-publicados'),
   ]

#------------------------------------------------------
#  Paths a instancias de usuario
#------------------------------------------------------
urlpatterns += [
   path('mispalabras/', views.PalabrasCreadasListView.as_view(), name='mis-palabras'),
   path('misrefranes/', views.RefranesCreadosListView.as_view(), name='mis-refranes'),
   ]

#------------------------------------------------------
#  Paths a instancias de usuario filtradas
#------------------------------------------------------
urlpatterns += [
   path('misenrevision/', views.RefranesenRevisionListView.as_view(), name='mis-refranes-enrevision'),
   path('misaprobados/', views.RefranesAprobadosListView.as_view(), name='mis-refranes-aprobados'),
   path('mispublicados/', views.RefranesPublicadosListView.as_view(), name='mis-refranes-publicados'),
   ]

#------------------------------------------------------
#  Paths a todas las instancias para administradores
#------------------------------------------------------
urlpatterns += [
   path('todasletras/', views.TodasLetrasListView.as_view(), name='todas-letras'),
   path('todosorigenes/', views.TodosOrigenesListView.as_view(), name='todos-origenes'),
   path('todaspalabras/', views.TodasPalabrasListView.as_view(), name='todas-palabras'),
   path('todosrefranes/', views.TodosRefranesListView.as_view(), name='todos-refranes'),
   ]


#------------------------------------------------------
#  Paths a todas con filtros de instancias
#------------------------------------------------------
urlpatterns += [
   path('todaspalabrasletra/<uuid:pk>', views.TodasPalabrasLetraListView.as_view(), name='todas-palabras-letra'),
   path('todosrefranespalabra/<uuid:pk>', views.TodosRefranesPalabraListView.as_view(), name='todos-refranes-palabra'),
   path('todosrefranesletra/<uuid:pk>', views.TodosRefranesLetraListView.as_view(), name='todos-refranes-letra'),
   ]
#------------------------------------------------------
#  Paths a operaciones de instancias para autorizados
#------------------------------------------------------
urlpatterns += [
   path('letra/crea/', views.LetraCrea.as_view(), name='letra-crea'),
   path('letra/<uuid:pk>/borra/', views.LetraBorra.as_view(), name='letra-borra'),
#   path('palabra/crea/', views.PalabraCrea.as_view(), name='palabra-crea'),
   path('palabra/nueva/', views.PalabraNueva, name='palabra-nueva'),
   path('palabra/<uuid:pk>', views.PalabraDetailView.as_view(), name='palabra-detalle'),
   path('palabra/<uuid:pk>/actualiza/', views.PalabraActualiza.as_view(), name='palabra-actualiza'),
   path('palabra/<uuid:pk>/borra/', views.PalabraBorra.as_view(), name='palabra-borra'),
#   path('refran/crea/', views.RefranCrea.as_view(), name='refran-crea'),
   path('refran/nuevo/', views.RefranNuevo, name='refran-nuevo'),
   path('refran/<uuid:pk>/actualiza/', views.RefranActualiza.as_view(), name='refran-actualiza'),
   path('refran/<uuid:pk>/borra/', views.RefranBorra.as_view(), name='refran-borra'),
   ]

#------------------------------------------------------
#  Paths de filtros de instancias
#------------------------------------------------------
urlpatterns += [
   path('palabrasletra/<uuid:pk>', views.PalabrasLetraListView.as_view(), name='palabras-letra'),
   path('refranespalabra/<uuid:pk>', views.RefranesPalabraListView.as_view(), name='refranes-palabra'),
   path('refranesletra/<uuid:pk>', views.RefranesLetraListView.as_view(), name='refranes-letra'),
   ]

#------------------------------------------------------
#  Paths de búsquedas y contacto
#------------------------------------------------------
urlpatterns += [
   path('buscar', views.buscar, name='buscar'),
   path('buscar_palabra', views.buscar_palabra, name='busca-palabra'),
   path('buscar_significado', views.buscar_significado, name='busca-significado'),
   path('buscar_dicho', views.buscar_dicho, name='busca-dicho'),
   path('buscar_explicacion', views.buscar_explicacion, name='busca-explicacion'),
   path('buscar_numero', views.buscar_numero, name='busca-numero'),
#   path('buscado/(<str:mibusqueda>)(<str:mibusqueda_palabra>)(<str:mibusqueda_significado>)(<str:mibusqueda_dicho>)(<str:mibusqueda_explicacion>)', views.RefranesBuscados.as_view(), name='refran-buscado'),
   path('buscada_palabra/<str:mibusqueda_palabra>', views.PalabraBuscada.as_view(), name='palabra-buscada'),
   path('buscado_significado/<str:mibusqueda_significado>', views.SignificadoBuscado.as_view(), name='significado-buscado'),
   path('buscado_dicho/<str:mibusqueda_dicho>', views.DichoBuscado.as_view(), name='dicho-buscado'),
   path('buscada_explicacion/<str:mibusqueda_explicacion>', views.ExplicacionBuscada.as_view(), name='explicacion-buscada'),
   path('buscado_numero/<str:mibusqueda_numero>', views.NumeroBuscado.as_view(), name='numero-buscado'),
   path('contacto/', views.contacto, name='contacto'),
   #path('gracias/(<str:remitente>)', views.Gracias, name='gracias'),
   path('gracias/', views.Gracias, name='gracias'),
   ]
#------------------------------------------------------
#  Paths de paginas de pruebas
#------------------------------------------------------
#from django.urls import re_path
urlpatterns += [
#   path('nuevo', views.indexnuevo),
#   path('nuevo/', views.indexnuevo),
#   path('new/', views.indexnew),
   ]
#------------------------------------------------------
#  Fin de los Paths
#------------------------------------------------------
