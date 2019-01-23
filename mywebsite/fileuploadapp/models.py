from django.db import models
from django_tables2 import tables

# Create your models here.
from django.urls import reverse


class FileUpload(models.Model):

    #the variable to take the inputs
    file = models.FileField()
    processed = models.BooleanField(default=False)

    # on submit click on the user entry page, it redirects to the url below.
    def get_absolute_url(self):
        return reverse('fileuploadapp:apphome')


class FileUploadTable(tables.Table):
    class Meta:
        model=FileUpload

class FileData(models.Model):
    sku = models.CharField(max_length=15)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
