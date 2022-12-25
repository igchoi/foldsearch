from django.urls import path

from . import views

urlpatterns = [
#    path('', views.index, name='index'), # views -> views.py
    path('', views.upload_file, name='upload_file')  #
]
