from django.conf.urls import url

#from fileuploadapp import views
from .views import *

app_name = 'fileuploadapp'

urlpatterns = [

    # fileuploadapp/
    url(r'^$', HomeView.as_view(), name='apphome'),
    # fileuploadapp/register
    url(r'^upload/$', FileUploadEntry.as_view(), name='fileupload'),

]

from django.shortcuts import reverse
