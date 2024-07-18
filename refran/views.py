
#------------------------------------------------------
#  Sección de importación de módulos
#------------------------------------------------------

import datetime
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.views.generic.list import MultipleObjectMixin

from .models import Letra, Origen, Palabra, Refran
import random
from datetime import datetime
from .forms import PalabraForm
from .forms import RefranForm
from .forms import BusquedaForm
from .forms import ContactForm

# Importamos las clases creadas en el archivo views_pdf
#from . import views_pdf

#------------------------------------------------------
#  Vista de Contacto
#------------------------------------------------------
def contacto(request):
   if request.method=="POST":
      form=ContactForm(request.POST)
      if form.is_valid():
         asunto = form.cleaned_data["asunto"]
         mensaje = form.cleaned_data["mensaje"]
         remitente = form.cleaned_data["remitente"]
         concopia = form.cleaned_data["concopia"]
         #recipients = ["lpdeonis@gmail.com"]
         recipients = []

         if concopia:
            recipients.append(remitente)

         #send_mail(asunto, mensaje, remitente, recipients)
         send_mail(asunto, mensaje, remitente, recipients, fail_silently=False)
         #gracias_url = reverse_lazy('gracias', kwargs={"remitente":remitente})
         gracias_url = reverse_lazy('gracias')
         return redirect(gracias_url)
         #return HttpResponseRedirect(gracias_url)

   else:
      form=ContactForm()
   return render(request, 'refran/contacto_form.html', {'form':form})

#def Gracias(request, **kwargs):
def Gracias(request):
   #remitente=kwargs['remitente']
   #sender=request.POST.get('sender', None)
   #context = {
   #   'remitente': remitente
   #   }
   #return render(request, 'refran/gracias.html', context=context)
   return render(request, 'refran/gracias.html')

#------------------------------------------------------
#  Vistas de Búsqueda
#------------------------------------------------------
def buscar(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda=request.POST.get('mibusqueda', None)
         mibusqueda_palabra=request.POST.get('mibusqueda_palabra', None)
         mibusqueda_significado=request.POST.get('mibusqueda_significado', None)
         mibusqueda_dicho=request.POST.get('mibusqueda_dicho', None)
         mibusqueda_explicacion=request.POST.get('mibusqueda_explicacion', None)
         success_url = reverse_lazy('refran-buscado', kwargs={"mibusqueda":mibusqueda,
            "mibusqueda_palabra":mibusqueda_palabra,
            "mibusqueda_significado":mibusqueda_significado,
            "mibusqueda_dicho":mibusqueda_dicho,
            "mibusqueda_explicacion":mibusqueda_explicacion
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'refran/busca_form.html', {'form':form})

def buscar_palabra(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_palabra=request.POST.get('mibusqueda_palabra', None)
         success_url = reverse_lazy('palabra-buscada', kwargs={
            "mibusqueda_palabra":mibusqueda_palabra
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'refran/busca_form.html', {'form':form})

def buscar_significado(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_significado=request.POST.get('mibusqueda_significado', None)
         success_url = reverse_lazy('significado-buscado', kwargs={
            "mibusqueda_significado":mibusqueda_significado
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'refran/busca_form.html', {'form':form})

def buscar_dicho(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_dicho=request.POST.get('mibusqueda_dicho', None)
         success_url = reverse_lazy('dicho-buscado', kwargs={
            "mibusqueda_dicho":mibusqueda_dicho
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'refran/busca_form.html', {'form':form})

def buscar_explicacion(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_explicacion=request.POST.get('mibusqueda_explicacion', None)
         success_url = reverse_lazy('explicacion-buscada', kwargs={
            "mibusqueda_explicacion":mibusqueda_explicacion
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'refran/busca_form.html', {'form':form})

def buscar_numero(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_numero=request.POST.get('mibusqueda_numero', None)
         success_url = reverse_lazy('numero-buscado', kwargs={
            "mibusqueda_numero":mibusqueda_numero
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'refran/busca_form.html', {'form':form})

# ---------
# Obsoleta
# --------
class RefranesBuscados(generic.ListView):
   template_name = 'refran/buscados_refranes.html'
   paginate_by = 10
   
   def get_queryset(self,**kwargs):
       self.mibusqueda=self.kwargs['mibusqueda']
       self.mibusqueda_palabra=self.kwargs['mibusqueda_palabra']
       self.mibusqueda_significado=self.kwargs['mibusqueda_significado']
       self.mibusqueda_dicho=self.kwargs['mibusqueda_dicho']
       self.mibusqueda_explicacion=self.kwargs['mibusqueda_explicacion']
       return Refran.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      context = super(RefranesBuscados,self).get_context_data(**kwargs)
      mibusqueda=self.kwargs['mibusqueda']
      mibusqueda_palabra=self.kwargs['mibusqueda_palabra']
      mibusqueda_significado=self.kwargs['mibusqueda_significado']
      mibusqueda_dicho=self.kwargs['mibusqueda_dicho']
      mibusqueda_explicacion=self.kwargs['mibusqueda_explicacion']
      if mibusqueda_palabra != None:
         context['mibusqueda_palabra']=self.mibusqueda_palabra
         context['resultado_palabra']=Palabra.objects.filter(palabra__icontains=self.mibusqueda_palabra).filter(estado__exact='a')
      if mibusqueda_significado != None:
         context['mibusqueda_significado']=self.mibusqueda_significado
         context['resultado_significado']=Palabra.objects.filter(significado__icontains=self.mibusqueda_significado).filter(estado__exact='a')
      if mibusqueda_dicho != None:
         context['mibusqueda_dicho']=self.mibusqueda_dicho
         context['resultado_dicho']=Refran.objects.filter(dicho__icontains=self.mibusqueda_dicho).filter(estado__exact='p')
      if mibusqueda_explicacion != None:
         context['mibusqueda_explicacion']=self.mibusqueda_explicacion
         context['resultado_explicacion']=Refran.objects.filter(explicacion__icontains=self.mibusqueda_explicacion).filter(estado__exact='p')
      return context

class PalabraBuscada(generic.ListView, MultipleObjectMixin):
   template_name = 'refran/buscada_palabra.html'
   paginate_by = 10
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_palabra=self.kwargs['mibusqueda_palabra']
       return Refran.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      object_list = Palabra.objects.filter(palabra__icontains=self.mibusqueda_palabra).filter(estado__exact='a')
      #context = super(PalabraBuscada,self).get_context_data(**kwargs)
      context = super(PalabraBuscada,self).get_context_data(object_list=object_list, **kwargs)
      mibusqueda_palabra=self.kwargs['mibusqueda_palabra']
      if mibusqueda_palabra != None:
         context['mibusqueda_palabra']=self.mibusqueda_palabra
         #context['resultado_palabra']=Palabra.objects.filter(palabra__icontains=self.mibusqueda_palabra).filter(estado__exact='a')
      return context

class SignificadoBuscado(generic.ListView, MultipleObjectMixin):
   template_name = 'refran/buscado_significado.html'
   paginate_by = 10
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_significado=self.kwargs['mibusqueda_significado']
       return Refran.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      object_list = Palabra.objects.filter(significado__icontains=self.mibusqueda_significado).filter(estado__exact='a')
      #context = super(SignificadoBuscado,self).get_context_data(**kwargs)
      context = super(SignificadoBuscado,self).get_context_data(object_list=object_list, **kwargs)
      mibusqueda_significado=self.kwargs['mibusqueda_significado']
      if mibusqueda_significado != None:
         context['mibusqueda_significado']=self.mibusqueda_significado
         #context['resultado_significado']=Palabra.objects.filter(significado__icontains=self.mibusqueda_significado).filter(estado__exact='a')
      return context

class DichoBuscado(generic.ListView, MultipleObjectMixin):
   template_name = 'refran/buscado_dicho.html'
   paginate_by = 10
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_dicho=self.kwargs['mibusqueda_dicho']
       return Refran.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      object_list = Refran.objects.filter(dicho__icontains=self.mibusqueda_dicho).filter(estado__exact='p')
      #context = super(DichoBuscado,self).get_context_data(**kwargs)
      context = super(DichoBuscado,self).get_context_data(object_list=object_list,**kwargs)
      mibusqueda_dicho=self.kwargs['mibusqueda_dicho']
      if mibusqueda_dicho != None:
         context['mibusqueda_dicho']=self.mibusqueda_dicho
         #context['resultado_dicho']=Refran.objects.filter(dicho__icontains=self.mibusqueda_dicho).filter(estado__exact='p')
      return context

class ExplicacionBuscada(generic.ListView, MultipleObjectMixin):
   template_name = 'refran/buscada_explicacion.html'
   paginate_by = 5
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_explicacion=self.kwargs['mibusqueda_explicacion']
       return Refran.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      object_list =Refran.objects.filter(explicacion__icontains=self.mibusqueda_explicacion).filter(estado__exact='p')
      #context = super(ExplicacionBuscada,self).get_context_data(**kwargs)
      context = super(ExplicacionBuscada,self).get_context_data(object_list=object_list, **kwargs)
      mibusqueda_explicacion=self.kwargs['mibusqueda_explicacion']
      if mibusqueda_explicacion != None:
         context['mibusqueda_explicacion']=self.mibusqueda_explicacion
         #context['resultado_explicacion']=Refran.objects.filter(explicacion__icontains=self.mibusqueda_explicacion).filter(estado__exact='p')
      return context

class NumeroBuscado(generic.ListView, MultipleObjectMixin):
   template_name = 'refran/buscado_numero.html'
   paginate_by = 10
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_numero=self.kwargs['mibusqueda_numero']
       return Refran.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      num_refranes_publicados = Refran.objects.filter(estado__exact='p').count()
      mibusqueda_numero=self.kwargs['mibusqueda_numero']
      if num_refranes_publicados >= int(mibusqueda_numero) and mibusqueda_numero != None:
         object_list = Refran.objects.filter(estado__exact='p').order_by('fecha').order_by('fechaaprobacion').order_by('fechapublicacion')[int(self.mibusqueda_numero)-1]
         #context = super(NumeroBuscado,self).get_context_data(object_list=object_list,**kwargs)
         context={
            'object_list':object_list
         }
         context['mibusqueda_numero']=self.mibusqueda_numero
      else:
         context={}
      return context

#------------------------------------------------------
#  Vista de función de index
#------------------------------------------------------
def index(request):
   num_letras = Letra.objects.all().count()
   num_origenes = Origen.objects.all().count()
   num_origenes_revision = Origen.objects.filter(estado__exact='r').count()
   num_origenes_aprobados = Origen.objects.filter(estado__exact='a').count()
   num_palabras = Palabra.objects.all().count()
   num_palabras_revision = Palabra.objects.filter(estado__exact='r').count()
   num_palabras_aprobadas = Palabra.objects.filter(estado__exact='a').count()
   num_refranes = Refran.objects.all().count()
   num_refranes_revision = Refran.objects.filter(estado__exact='r').count()
   num_refranes_aprobados = Refran.objects.filter(estado__exact='a').count()
   num_refranes_publicados = Refran.objects.filter(estado__exact='p').count()
   num_visitas = request.session.get('num_visitas', 0)
   #fecha=datetime.now().today()
   dt = datetime.now()
   fecha_ano = dt.year
   fecha_mes = dt.month
   fecha_dia = dt.day
   fecha='%s%s%s' % (fecha_ano,fecha_mes,fecha_dia)
   resto=str(int(fecha)%int(num_refranes_publicados))

   if (num_refranes_publicados !=0):
      num_aleatorio=random.randint(1, num_refranes_publicados)
      refran_aleatorio=Refran.objects.filter(estado__exact='p').order_by('fecha').order_by('fechaaprobacion').order_by('fechapublicacion')[num_aleatorio-1]
      refran_dicho=refran_aleatorio.dicho
      refran_explicacion=refran_aleatorio.explicacion
      refran_palabra=refran_aleatorio.palabra.palabra
      refran_palabra_id=refran_aleatorio.palabra.id
      refran_deldia=Refran.objects.filter(estado__exact='p').order_by('fecha').order_by('fechaaprobacion').order_by('fechapublicacion')[int(resto)-1]

   else:
      refran_dicho=""
      refran_explicacion=""
      num_aleatorio=0
   context = {
      'num_letras': num_letras,
      'num_origenes':num_origenes,
      'num_origenes_revision':num_origenes_revision,
      'num_origenes_aprobados':num_origenes_aprobados,
      'num_palabras':num_palabras,
      'num_palabras_revision':num_palabras_revision,
      'num_palabras_aprobadas':num_palabras_aprobadas,
      'num_refranes':num_refranes,
      'num_refranes_revision': num_refranes_revision,
      'num_refranes_aprobados': num_refranes_aprobados,
      'num_refranes_publicados': num_refranes_publicados,
      'refran_aleatorio':refran_aleatorio.id,
      'refran_numero':num_aleatorio,
      'refran_dicho':refran_dicho,
      'refran_palabra':refran_palabra,
      'refran_palabra_id':refran_palabra_id,
      'refran_explicacion':refran_explicacion,
      #'fecha':fecha,
      #'fecha_ano':fecha_ano,
      #'fecha_mes':fecha_mes,
      #'fecha_dia':fecha_dia,
      #'resto':resto,
      'refran_deldia':refran_deldia,
      }
   return render(request, 'index.html', context=context)

def notas(request):
   num_letras = Letra.objects.all().count()
   num_origenes = Origen.objects.all().count()
   num_palabras = Palabra.objects.all().count()
   num_refranes = Refran.objects.all().count()
   num_proverbios = Refran.objects.filter(explicacion__icontains='proverbio').count()
   context = {
      'num_letras': num_letras,
      'num_origenes':num_origenes,
      'num_palabras':num_palabras,
      #'num_refranes':num_refranes-num_proverbios,
      'num_refranes':num_refranes,
      'num_proverbios':num_proverbios,
      }
   return render(request, 'notas.html', context=context)
#------------------------------------------------------
#  Vistas de Letra
#------------------------------------------------------
class LetraListView(generic.ListView):
   model = Letra
   #def get_queryset(self):
   #   return(
   #      Letra.objects.all()
   #      )

class x_LetraDetailView(generic.DetailView):
   model = Letra

class LetraDetailView(generic.DetailView, MultipleObjectMixin):
   model = Letra
   template = "refran/letra_detail.html"
   paginate_by = 10

   def get_context_data(self, **kwargs):
      object_list = Palabra.objects.filter(letra=self.get_object())
      context = super(LetraDetailView, self).get_context_data(object_list=object_list, **kwargs)
      return context

#------------------------------------------------------
#  Vistas de Origen
#------------------------------------------------------
class OrigenListView(generic.ListView):
   model = Origen
   def get_queryset(self):
      return(
         Origen.objects.filter(estado__exact='a').order_by('fecha')
         )

class x_OrigenDetailView(generic.DetailView):
   model = Origen

from django.db.models import Value

class OrigenDetailView(generic.DetailView, MultipleObjectMixin):
   model = Origen
   template = "refran/origen_detail.html"
   paginate_by = 20

   def get_context_data(self, **kwargs):
#      object_list = Palabra.objects.filter(origen=self.get_object())
#      palabra_list = Palabra.objects.filter(origen=self.get_object()).filter(estado__exact='a')
#      palabra_list = Palabra.objects.filter(origen=self.get_object()).only('id','palabra','significado')
      palabra_list = Palabra.objects.filter(origen=self.get_object()).values('id','palabra','significado').annotate(tipo=Value(0))
#      refran_list = Refran.objects.filter(origen=self.get_object()).filter(estado__exact='p')
#      refran_list = Refran.objects.filter(origen=self.get_object()).only('id','dicho','explicacion')
      refran_list = Refran.objects.filter(origen=self.get_object()).values('id','dicho','explicacion').annotate(tipo=Value(1))
      cnt_palabras= Palabra.objects.filter(origen=self.get_object()).count()
      object_list = palabra_list.union(refran_list)
      #object_list = refran_list.union(palabra_list)
      #object_list = refran_list.annotate(tipo=Value(1))
      #object_list = refran_list.aggregate(tipo=Value(1))
#      object_list = refran_list
      context = super(OrigenDetailView, self).get_context_data(object_list=object_list, **kwargs)
#      context['palabra_list']=palabra_list
#      context['refran_list']=refran_list
#      context += refran_list
#      return context.order_by('letra').order_by('palabra')
      #context['campos']=list(object_list.values()[0])
      context['origen']=self.get_object()
      context['cnt_palabras']=cnt_palabras
      context['campos']=object_list._fields
      return context

#------------------------------------------------------
#  Vistas de Palabra
#------------------------------------------------------
class PalabraListView(generic.ListView):
   model = Palabra
   paginate_by = 30
   def get_queryset(self):
      return(
         Palabra.objects.filter(estado__exact='a').order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(PalabraListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      return context

#class PalabraDetailView(generic.DetailView):
#   model = Palabra

class PalabraDetailView(generic.DetailView, MultipleObjectMixin):
   model = Palabra
   template = "refran/palabra_detail.html"
   paginate_by = 5

   def get_context_data(self, **kwargs):
      object_list = Refran.objects.filter(palabra=self.get_object())
      context = super(PalabraDetailView, self).get_context_data(object_list=object_list, **kwargs)
      return context

#------------------------------------------------------
#  Vistas de Refrán
#------------------------------------------------------
class RefranListView(generic.ListView):
   model = Refran
   paginate_by = 10
   def get_queryset(self):
      result=Refran.objects.filter(estado__exact='p')
      return(
         result.order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(RefranListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      context['palabras']=Palabra.objects.all
      return context

class RefenRevisionListView(generic.ListView):
   model = Refran
   template_name = 'refran/refranes_enrevision_list.html'
   paginate_by = 10
   def get_queryset(self):
      return(
         Refran.objects.filter(estado__exact='r').order_by('palabra')
         )

class RefAprobadosListView(generic.ListView):
   model = Refran
   template_name = 'refran/refranes_aprobados_list.html'
   paginate_by = 10
   def get_queryset(self):
      return(
         Refran.objects.filter(estado__exact='a').order_by('palabra')
         )

class RefPublicadosListView(generic.ListView):
   model = Refran
   template_name = 'refran/refranes_publicados_list.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.filter(estado__exact='p').order_by('palabra')
         )

class RefranDetailView(generic.DetailView):
   model = Refran

#------------------------------------------------------------
#  Vistas de Palabras y Refranes Creados por Usuario
#------------------------------------------------------------
from django.contrib.auth.mixins import LoginRequiredMixin

class PalabrasCreadasListView(LoginRequiredMixin, generic.ListView):

   model = Palabra
   template_name = 'refran/palabrascreadas_por_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return (
         Palabra.objects.filter(creador=self.request.user).order_by('palabra')
         )

class RefranesCreadosListView(LoginRequiredMixin, generic.ListView):

   model = Refran
   template_name = 'refran/refranescreados_por_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.filter(creador=self.request.user).order_by('palabra')
         )

class RefranesenRevisionListView(LoginRequiredMixin, generic.ListView):

   model = Refran
   template_name = 'refran/refranesenrevision_de_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.filter(creador=self.request.user).filter(estado__exact='r').order_by('palabra')
         )
class RefranesAprobadosListView(LoginRequiredMixin, generic.ListView):

   model = Refran
   template_name = 'refran/refranesaprobados_de_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.filter(creador=self.request.user).filter(estado__exact='a').order_by('palabra')
         )
class RefranesPublicadosListView(LoginRequiredMixin, generic.ListView):

   model = Refran
   template_name = 'refran/refranespublicados_de_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.filter(creador=self.request.user).filter(estado__exact='p').order_by('palabra')
         )

#------------------------------------------------------------
#  Vistas de Letras, Orígenes, Palabras y Refranes Totales
#------------------------------------------------------------
class TodasLetrasListView(LoginRequiredMixin, generic.ListView):

   model = Letra
   template_name = 'refran/todas_letras.html'

   def get_queryset(self):
      return(
         Letra.objects.all()
         )

class TodosOrigenesListView(LoginRequiredMixin, generic.ListView):
   model = Origen
   template_name = 'refran/todos_origenes.html'

   def get_queryset(self):
      return(
         Origen.objects.all().order_by('fecha')
         )

class TodasPalabrasListView(LoginRequiredMixin, generic.ListView):
   model = Palabra
   template_name = 'refran/todas_palabras.html'
   paginate_by = 30

   def get_queryset(self):
      return(
         Palabra.objects.all().order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(TodasPalabrasListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      return context

class TodosRefranesListView(LoginRequiredMixin, generic.ListView):
   model = Refran
   template_name = 'refran/todos_refranes.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.all().order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(TodosRefranesListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      context['palabras']=Palabra.objects.all
      return context

#from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Palabra, Refran
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect

#------------------------------------------------------------
#  Vistas de edición de Letras
#------------------------------------------------------------
class LetraCrea(PermissionRequiredMixin, CreateView):
   model = Letra
   fields=['letra']
   permission_required='refran.add_letra'

class LetraBorra(PermissionRequiredMixin,DeleteView):
   model = Letra
   success_url = reverse_lazy('letras')
   permission_required='refran.delete_letra'

   def form_valid(self, form):
      try:
         self.object.delete()
         return HttpResponseRedirect(self.success_url)
      except:
         reverse("letra-borra", kwargs={"pk":self.object.pk})

#------------------------------------------------------------
#  Vistas de edición de Palabras
#------------------------------------------------------------
#class PalabraCrea(PermissionRequiredMixin, CreateView):
#   model = Palabra
#   fields=['palabra', 'significado', 'letra', 'fecha', 'origen', 'creador', 'estado']
##   fieldsets = (
##      (None, {'fields': ('palabra', 'significado')}),
##      ('Detalle', {'fields': ('estado',('fecha', 'creador'),('letra','origen'))}),
##      )
#   permission_required='refran.add_palabra'

def PalabraNueva(request):
   if request.method=="POST":
      form=PalabraForm(request.POST)
      if form.is_valid():
         palabra=form.save(commit=False)
         palabra.creador=request.user
#         palabra.fecha=date.today
         palabra.save()
         success_url = reverse_lazy('palabra-detalle', kwargs={"pk":palabra.pk})
         return redirect(success_url)
   else:
      form=PalabraForm()
   return render(request,'refran/palabra_nueva.html', {'form':form})

   def no_repetida(self):
      buscada=Palabra.objects.filter(palabra__exact=self.palabra)
      if buscada:
         return(False)
      return(True)

class PalabraActualiza(PermissionRequiredMixin,UpdateView):
   model = Palabra
   fields=['palabra', 'significado', 'letra', 'fecha', 'origen', 'creador', 'estado']
   permission_required='refran.change_palabra'

class PalabraBorra(PermissionRequiredMixin,DeleteView):
   model = Palabra
   success_url = reverse_lazy('palabras')
   permission_required='refran.delete_palabra'

   def form_valid(self, form):
      try:
         self.object.delete()
         return HttpResponseRedirect(self.success_url)
      except:
         reverse("palabra-borra", kwargs={"pk":self.object.pk})

#------------------------------------------------------------
#  Vistas de edición de Refranes
#------------------------------------------------------------
#class RefranCrea(PermissionRequiredMixin, CreateView):
#   model = Refran
#   fields=['dicho', 'explicacion', 'fecha', 'fechaaprobacion', 'fechapublicacion', 'estado', 'letra', 'palabra', 'origen', 'creador']
#   permission_required='refran.add_refran'
#

def RefranNuevo(request):
   if request.method=="POST":
      form=RefranForm(request.POST)
      if form.is_valid():
         refran=form.save(commit=False)
         refran.creador=request.user
#         palabra.fecha=date.today
         estado=request.POST.get('estado', None)
         fecha=datetime.now().today()
         if estado == 'r':
            refran.fecha=fecha
         if estado == 'a':
            refran.fecha=fecha
            refran.fechaaprobacion=fecha
         if estado == 'p':
            refran.fecha=fecha
            refran.fechaaprobacion=fecha
            refran.fechapublicacion=fecha
         refran.save()
         success_url = reverse_lazy('refran-detalle', kwargs={"pk":refran.pk})
         return redirect(success_url)
   else:
      form=RefranForm()
   return render(request,'refran/refran_nuevo.html', {'form':form})

class RefranActualiza(PermissionRequiredMixin,UpdateView):
   model = Refran
   fields=['dicho', 'explicacion', 'fecha', 'fechaaprobacion', 'fechapublicacion', 'estado', 'letra', 'palabra', 'origen', 'creador']
   permission_required='refran.change_refran'

class RefranBorra(PermissionRequiredMixin,DeleteView):
   model = Refran
   success_url = reverse_lazy('refranes')
   permission_required='refran.delete_refran'

   def form_valid(self, form):
      try:
         self.object.delete()
         return HttpResponseRedirect(self.success_url)
      except:
         reverse("refran-borra", kwargs={"pk":self.object.pk})

from django.shortcuts import get_object_or_404
#------------------------------------------------------------
#  Vistas de filtros
#------------------------------------------------------------
class PalabrasLetraListView(generic.ListView):
   model = Palabra
   template_name = 'refran/palabras_de_letra.html'
   paginate_by = 30
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       return Palabra.objects.filter(letra=self.letra).filter(estado__exact='a')

   def get_context_data(self, **kwargs):
      context = super(PalabrasLetraListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      context['letra']=self.letra
      return context

class RefranesPalabraListView(generic.ListView):
   model = Refran
   template_name = 'refran/refranes_de_palabra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.palabra=get_object_or_404(Palabra,id=self.kwargs["pk"])
       return Refran.objects.filter(palabra=self.palabra).filter(estado__exact='p')

   def get_context_data(self, **kwargs):
      context = super(RefranesPalabraListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      context['palabras']=Palabra.objects.all
      context['palabra']=self.palabra
      return context

class RefranesLetraListView(generic.ListView):
   model = Refran
   template_name = 'refran/refranes_de_letra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       palabras=Palabra.objects.filter(letra=self.letra).filter(estado__exact='a')
       return Refran.objects.filter(palabra__in=palabras).filter(estado__exact='p')

   def get_context_data(self, **kwargs):
      context = super(RefranesLetraListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      context['palabras']=Palabra.objects.filter(letra=self.kwargs["pk"])
      context['letra']=self.letra
      return context

#------------------------------------------------------------
#  Vistas de filtros para todas y todos (Administración)
#------------------------------------------------------------
class TodasPalabrasLetraListView(generic.ListView):
   model = Palabra
   template_name = 'refran/todas_palabras_de_letra.html'
   paginate_by = 30
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       return Palabra.objects.filter(letra=self.letra)

   def get_context_data(self, **kwargs):
      context = super(TodasPalabrasLetraListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      context['letra']=self.letra
      return context

class TodosRefranesPalabraListView(generic.ListView):
   model = Refran
   template_name = 'refran/todos_refranes_de_palabra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.palabra=get_object_or_404(Palabra,id=self.kwargs["pk"])
       return Refran.objects.filter(palabra=self.palabra)

   def get_context_data(self, **kwargs):
      context = super(TodosRefranesPalabraListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      context['palabras']=Palabra.objects.all
      context['palabra']=self.palabra
      return context

class TodosRefranesLetraListView(generic.ListView):
   model = Refran
   template_name = 'refran/todos_refranes_de_letra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       palabras=Palabra.objects.filter(letra=self.letra)
       return Refran.objects.filter(palabra__in=palabras)

   def get_context_data(self, **kwargs):
      context = super(TodosRefranesLetraListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      context['palabras']=Palabra.objects.filter(letra=self.kwargs["pk"])
      context['letra']=self.letra
      return context

#------------------------------------------------------------
#  Fin de definición de Vistas
#------------------------------------------------------------
