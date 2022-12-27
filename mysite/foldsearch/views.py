from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
import os


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
    HttpResponse("ok, file uploaded and archived!")
    checkcmd = foldsearch(fname)
    if checkcmd == 0:
        if os.path.isfile('foldsearch/templates/result.html'):
            return render(request, 'result.html')
        else:
            return HttpResponse("Sorry, no result.. please run again..")
    else:
        return HttpResponse("Something wrong in your input file.. please run again")

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
    cmd = 'foldseek easy-search foldsearch/static/' + fn + ' foldsearch/static result.html tmp --format-mode 3'
    print(cmd)
    returned_value = os.system(cmd)  # returns the exit code in unix
    print(returned_value)
    if returned_value == 0:
        moved_value = os.system("mv result.html foldsearch/templates/")
        if moved_value == 0:
            return moved_value
    else:
        return 1


