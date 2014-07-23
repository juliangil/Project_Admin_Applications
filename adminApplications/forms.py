from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from adminDeviceApp.models import Device, Application, deviceApp
#from adminDeviceApp.models import Tipo
 
 
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }

 
class newDeviceForm(ModelForm):
	class Meta:
		model = Device
		fields = ['nombre', 'ip', 'tipo', 'estado']	

class newApplicationForm(ModelForm):
	class Meta:
		model = Application
		fields = ['nombre']	