from django.contrib import admin
from .models import Device, Application, deviceApp
#from .models import Tipo

admin.site.register(Device)
admin.site.register(Application)
#admin.site.register(Tipo)
admin.site.register(deviceApp)
