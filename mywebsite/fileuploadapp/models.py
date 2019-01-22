from django.db import models
from django_tables2 import tables

# Create your models here.
from django.urls import reverse


class FileUpload(models.Model):

    #the variable to take the inputs
    file = models.FileField()

    # on submit click on the user entry page, it redirects to the url below.
    def get_absolute_url(self):
        return reverse('fileuploadapp:apphome')


class FileUploadTable(tables.Table):
    class Meta:
        model=FileUpload
