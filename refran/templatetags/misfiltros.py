
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
import re

register=template.Library()

def es_primo(value,max):
   primo=True
   if value<=max:
      for i in range(2,value-1):
         if (value%i==0):
            primo=False
            break
   else:
      primo=False
   return primo

@register.filter(name='minuscula')
@stringfilter
def miniscula(value):
   return value.lower()

@register.filter(name='mayuscula')
@stringfilter
def mayuscula(value):
   return value.upper()

@register.filter(name='concatena')
@stringfilter
def concatena(value,cadena):
   return '%s%s' % (value,cadena)

#@register.filter(name='resalta', is_Safe=True, needs_autoescape=True)
@register.filter(name='resalta', is_Safe=True)
@stringfilter
def resalta(value, cadena):
   wordsList = value.split()
   for index, word in enumerate(wordsList):
      if word == cadena:
         #reemplazar_por='<span style="color:white;background-color:green">%s</span>' % cadena
         reemplazar_por='<span style="color:green">%s</span>' % cadena
         wordsList[index] = reemplazar_por
      elif word.lower() == cadena.lower():
         #reemplazar_por='<span style="color:white;background-color:red">%s</span>' % word
         reemplazar_por='<span style="color:red">%s</span>' % word
         wordsList[index] = reemplazar_por
      elif cadena in word:
         #reemplazar_por='<span style="color:white;background-color:blue">%s</span>' % cadena
         reemplazar_por='<span style="color:purple">%s</span>' % cadena
         nueva_cadena=word.replace(cadena,reemplazar_por)
         wordsList[index] = nueva_cadena
      elif cadena.lower() in word.lower():
         inicio=word.lower().find(cadena.lower())
         fin=inicio+len(cadena)
         result=word[inicio:fin]
         #reemplazar_por='<span style="color:white;background-color:orange">%s</span>' % result
         reemplazar_por='<span style="color:orange">%s</span>' % result
         nueva_cadena=word.lower().replace(cadena.lower(),reemplazar_por)
         wordsList[index] = nueva_cadena
   result = " ".join([word for word in wordsList])
   return mark_safe(result)

@stringfilter

@register.filter(name='resaltayenlaza', is_Safe=True)
def resaltayenlaza(value, args):
   (cadena,enlace) = args.split()
   wordsList = value.split()
   for index, word in enumerate(wordsList):
      if word == cadena:
         #reemplazar_por='<span style="color:green">%s</span>' % cadena
         reemplazar_por='<a href="palabra/%s"><span style="color:green">%s</span></a>' % (enlace,cadena)
         wordsList[index] = reemplazar_por
      elif word.lower() == cadena.lower():
         #reemplazar_por='<span style="color:red">%s</span>' % word
         reemplazar_por='<a href="palabra/%s"><span style="color:red">%s</span></a>' % (enlace,word)
         wordsList[index] = reemplazar_por
      elif cadena in word:
         #reemplazar_por='<span style="color:purple">%s</span>' % cadena
         reemplazar_por='<a href="palabra/%s"><span style="color:purple">%s</span></a>' % (enlace,cadena)
         nueva_cadena=word.replace(cadena,reemplazar_por)
         wordsList[index] = nueva_cadena
      elif cadena.lower() in word.lower():
         inicio=word.lower().find(cadena.lower())
         fin=inicio+len(cadena)
         result=word[inicio:fin]
         #reemplazar_por='<span style="color:orange">%s</span>' % result
         reemplazar_por='<a href="palabra/%s"><span style="color:orange">%s</span></a>' % (enlace,result)
         nueva_cadena=word.lower().replace(cadena.lower(),reemplazar_por)
         wordsList[index] = nueva_cadena
   result = " ".join([word for word in wordsList])
   return mark_safe(result)

@register.filter(name='activa_primo', is_Safe=True)
@stringfilter
def activa_primo(value):
   if es_primo(int(value),7777):
      result = '<span alt="4L0uP" class="blink"><span>%s</span></span>' % value
      return mark_safe(result)
   else:
      return value

@register.filter(name='enlaza', is_Safe=True)
@stringfilter
def enlaza(value, cadena):
   return "<a href=palabra/%s>%s</a>" % (cadena,value)

def enlazar(value, cadena):
   wordsList = value.split()
   for index, word in enumerate(wordsList):
      if value in word:
         reemplazar_por="<a href=\"%s\">%s</a>" % (cadena,word)
         wordsList[index] = reemplazar_por
      else:
         wordsList[index] = word
   result = " ".join([word for word in wordsList])
   #return mark_safe(result)
   return result



@register.filter(name='resaltar', is_Safe=True)
@stringfilter
def resaltar(value, cadena, autoescape=True):
#   return ' -> %s <- ' % value
#   if autoescape:
#      esca=conditional_escape
#   else:
#      esca = lambda x:x
#   reemplazar_por=esca('<span style="color:white;background-color:red">%s</span>' % cadena)
   reemplazar_por='<span style="color:white;background-color:red">%s</span>' % cadena
   result = value.replace(cadena,reemplazar_por)
   return mark_safe(result)

@register.filter(name='letrainicial', is_Safe=True, needs_autoescape=True)
@stringfilter
def letrainicial(value, autoescape=True):
   letra, demas = value[0], value[1:]
   if autoescape:
      esca = conditional_escape
   else:
      esca = lambda x: x
   result = '<strong>%s</strong>%s' % (esca(letra.upper()), esca(demas))
   return mark_safe(result)


