# -*- coding: utf-8 -*-
from django import forms
from django.forms import FileInput

class UploadFileForm(forms.Form):
    cargar  = forms.FileField(        
	label="Carga de archivo",
    )
