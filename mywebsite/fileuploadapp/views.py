from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic import CreateView

from .models import FileUpload, FileUploadTable


class HomeView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'file_list'
    template_name = 'fileuploadapp/home_page.html'

    def get_queryset(self):
        #import pdb;pdb.set_trace()
        table = FileUploadTable(FileUpload.objects.all())
        return table


# view for the user entry page
class FileUploadEntry(CreateView):
    model = FileUpload
    fields = ['file']
    template_name = 'fileuploadapp/user_form.html'
