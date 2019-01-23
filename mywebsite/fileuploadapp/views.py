from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .models import FileUpload, FileUploadTable, FileData


class HomeView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'file_list'
    template_name = 'fileuploadapp/home_page.html'

    def get_queryset(self):
        table = FileUploadTable(FileUpload.objects.all())
        return table


# view for the user entry page
class FileUploadEntry(CreateView):
    model = FileUpload
    fields = ['file']
    template_name = 'fileuploadapp/user_form.html'

    def process_file(self, obj):
        file_obj = obj.file
        records=list()
        lines = file_obj.readlines()
        for eachline in lines:
            line = eachline.strip()
            if line:
                linedata = eval(line)
                records.append(FileData(sku=linedata[0], name=linedata[1], price=linedata[2]))
        process=False
        if records:
            FileData.objects.bulk_create(records)
            process=True
        finstance = FileUpload.objects.get(file=file_obj)
        finstance.processed = process
        finstance.save()

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        self.process_file(instance)
        return HttpResponseRedirect("/home")
