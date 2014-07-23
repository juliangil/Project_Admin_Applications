from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'adminApplications.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'adminApplications.views.hello'), 

    # Activamos la url de los mediafiles

    url(r'^$','adminApplications.views.principal', name='principal'),
    url(r'^principal/','adminApplications.views.principal', name='principal'),
    url(r'^nuevoUsuario/', 'adminApplications.views.nuevoUsuario', name='nuevoUsuario'),
    url(r'^login/', login, {'template_name': 'login.html', }, name="login"),
    url(r'^inicio/', 'adminApplications.views.inicio', name='inicio'),
    url(r'^newDevice/', 'adminApplications.views.newDevice', name='newDevice'),
    url(r'^newApplication/', 'adminApplications.views.newApplication', name='newApplication'),
    

    url(r'^loginMuk/', 'adminApplications.views.loginMuk', name='loginMuk'),
    url(r'^inicioMuk/', 'adminApplications.views.inicioMuk', name='inicioMuk'),
    url(r'^registerMuk/', 'adminApplications.views.registerMuk', name='registerMuk'),
    url(r'^newDeviceMuk/', 'adminApplications.views.newDeviceMuk', name='newDeviceMuk'),
    url(r'^newApplication/', 'adminApplications.views.newApplicationMuk', name='newApplicationMuk'),
    url(r'^allDevices/', 'adminApplications.views.allDevicesMuk', name='allDevicesMuk'),
    url(r'^allApplications/', 'adminApplications.views.allApplicationsMuk', name='allApplicationsMuk'),
    url(r'^oneDevice/', 'adminApplications.views.oneDeviceMuk', name='oneDeviceMuk'),
    url(r'^oneApplication/', 'adminApplications.views.oneApplicationMuk', name='oneApplicationMuk'),
    url(r'^installApplications/', 'adminApplications.views.installApplicationsMuk', name='installApplicationsMuk'),
    url(r'^deviceDetails/', 'adminApplications.views.deviceDetailsMuk', name='deviceDetailsMuk'),
    url(r'^applicationDetails/', 'adminApplications.views.applicationDetailsMuk', name='applicationDetailsMuk'),

]