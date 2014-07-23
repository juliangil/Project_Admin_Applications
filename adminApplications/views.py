from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext

from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from forms import SignUpForm, newDeviceForm, newApplicationForm
from adminDeviceApp.models import Device, Application, deviceApp

def hello(request): #request: Solicitud por convencion y es una instancia de a clase django.http.HttpRequest
    return HttpResponse("Hello world") 

def principal(request):
    return render_to_response('principal.html', {}, context_instance=RequestContext(request))
 
def nuevoUsuario(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # Mira si todas las reglas de validacion pasan
 
            # Borra las variables del formulario forms.py
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
 
            # Crea uns usuario en la base de datos con los datos que le 
            # pasemos
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
 
            # Guarda en la base de datos
            user.save()
 
            return HttpResponseRedirect(reverse('principal'))  
            # Retornda despues del post, pero como esta en nuevoUsuario, el reverse
            # hace que retorne a la pagina anterior en este caso principal

    else:
        form = SignUpForm()
 
    formulario = {'form': form,}
    return render_to_response('login2.html', formulario, context_instance=RequestContext(request))

#En esta vista hemos hecho uso del decorador login_required() para indicar 
#que dicha vista solo sera accesible para usuarios que hayan hecho el login 
#correctamente, si un usuario intenta acceder a esta vista escribiendo la 
#ruta y no ha iniciado sesion en el sitio sera redirigido a la variable 
#LOGIN_URL que hemos definido anteriormente en el fichero settings.py.

@login_required()
def inicio(request):
    return render_to_response('inicio.html', {'user': request.user}, context_instance=RequestContext(request))

def newDevice(request):
    #si es una peticion post
    if request.method == "POST":
        #asignamos a form el formulario para validar
        form = newDeviceForm(request.POST)
        #si el formulario es validado correctamente
        if form.is_valid():
            #creamos una nueva instancia de Post con los campos del form
            #asi capturamos los valores post
            #newDevice = Device(nombre = request.POST["nombre"], ip = request.POST["ip"], estado = request.POST["estado"])
            newDevice = Device(nombre = form.cleaned_data["nombre"], ip = form.cleaned_data["ip"], estado = form.cleaned_data["estado"], tipo = form.cleaned_data["tipo"])
            #guardamos el post
            newDevice.save()
            #redirigimos a la ruta con name newDevice, que es esta
            return HttpResponseRedirect(reverse('inicio'))
    else:
        #si no es una peticion post, asignamos a form 
        #el form que hemos creado sin datos
        form = newDeviceForm()
    #siempre devolvemos la misma respuesta
    return render_to_response("newDevice.html",{"form":form}, context_instance = RequestContext(request))

def newApplication(request):
    #si es una peticion post
    if request.method == "POST":
        #asignamos a form el formulario para validar
        form = newApplicationForm(request.POST)
        #si el formulario es validado correctamente
        if form.is_valid():
            #creamos una nueva instancia de Post con los campos del form
            #asi capturamos los valores post
            #newDevice = Device(nombre = request.POST["nombre"], ip = request.POST["ip"], estado = request.POST["estado"])
            newApplication = Application(nombre = form.cleaned_data["nombre"])
            #guardamos el post
            newApplication.save()
            #redirigimos a la ruta con name newDevice, que es esta
            return HttpResponseRedirect(reverse('inicio'))
    else:
        #si no es una peticion post, asignamos a form 
        #el form que hemos creado sin datos
        form = newApplicationForm()
    #siempre devolvemos la misma respuesta
    return render_to_response("newApplication.html",{"form":form}, context_instance = RequestContext(request))

def loginMuk(request):
    return render_to_response('loginMuk.html')

def inicioMuk(request):
    return render_to_response('inicioMuk.html')

def registerMuk(request):
    return render_to_response('registerMuk.html')

def newDeviceMuk(request):
    return render_to_response('newDeviceMuk.html')

def newApplicationMuk(request):
    return render_to_response('newApplicationMuk.html')

def allDevicesMuk(request):
    return render_to_response('allDevicesMuk.html')

def allApplicationsMuk(request):
    return render_to_response('allApplicationsMuk.html')

def oneDeviceMuk(request):
    return render_to_response('oneDeviceMuk.html')

def oneApplicationMuk(request):
    return render_to_response('oneApplicationMuk.html')

def installApplicationsMuk(request):
    return render_to_response('installApplicationsMuk.html')

def deviceDetailsMuk(request):
    return render_to_response('deviceDetailsMuk.html')

def applicationDetailsMuk(request):
    return render_to_response('applicationDetailsMuck.html')