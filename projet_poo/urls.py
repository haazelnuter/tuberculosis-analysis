from . import views
from django.urls import path

urlpatterns = [path('', views.home),
               path('connexion', views.index, name='connexion'),
               path('patient', views.patient, name='form'),
               path('visualisation', views.patientView, name='datavis')]
