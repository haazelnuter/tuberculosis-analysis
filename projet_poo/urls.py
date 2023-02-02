from . import views
from django.urls import path

urlpatterns = [path('', views.index),
               path('connexion', views.index, name='connexion'),
               path('patient', views.patient, name='form'),
               path('visualisation', views.patientView, name='datavis'),
               path('patients', views.home, name="patients")]
