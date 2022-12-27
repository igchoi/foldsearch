from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'upload.html')
#    return HttpResponse("Hello, World!")
