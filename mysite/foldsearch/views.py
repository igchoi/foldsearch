from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse

def index(request):
    return render(request, 'pdb.html')
#    return HttpResponse("Hello, World!")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
          #  return HttpResponseRedirect('/success/url/')
            return HttpResponse("Successfully uploaded & saved")
    else:
        form = UploadFileForm()
    return render(request, 'pdb.html', {'form': form})

def handle_uploaded_file(f):
    with open('tmp.pdb', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
