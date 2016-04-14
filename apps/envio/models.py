from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FileSave(models.Model):
    mi_archivo = models.FileField(upload_to='media/files/')
