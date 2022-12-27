from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse


def index(request):
    return render(request, 'pdb.html')
#    return HttpResponse("Hello, World!")


def upload_file(request):
    #   for k in request.FILES.keys():
    #       print(k)
    #   file = request.FILES['fileInput']
    fname = request.FILES['fileInput'].name
    print("# file name: ", fname)  # 'fileInput' is a form tag (name) in HTML
    handle_uploaded_file(request.FILES['fileInput'], fname)
    return HttpResponse("ok, file uploaded and archived!")

# this is for {'form': form} handling in forms.py
#    if request.method == 'POST':
#        form = UploadFileForm(request.FILES)
#        if form.is_valid():
#            handle_uploaded_file(request.FILES['fileInput'])
#          #  return HttpResponseRedirect('/success/url/')
#            return HttpResponse("Successfully uploaded & saved")
#    else:
#        form = UploadFileForm()
#        return HttpResponse("Failed to upload")
#    return render(request, 'pdb.html', {'form': form})
#    return render(request, 'pdb.html')


def handle_uploaded_file(f, fn):
    with open('foldsearch/static/'+fn, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def foldsearch(fn):
