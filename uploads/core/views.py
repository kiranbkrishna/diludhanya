from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm

import dbx
import uuid
from django.conf import settings
#from settings import IMAGE_DIR
def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        dest_path = settings.MEDIA_URL + str(uuid.uuid4()) + '.jpg'
        #write to tempfile

        if myfile:
            fs = FileSystemStorage()
            print dest_path
            filename = fs.save(dest_path, myfile)

             # myfile = fs.save(dest_path, picture)
        #file = tempfile.TemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None)
            
       

        uploaded_file_url = fs.url(filename)
        dbx.db_upload(uploaded_file_url)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def dbox_upload():

    pass

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
