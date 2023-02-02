import os

import cv2
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render, redirect
from .models import AddPatient

from keras.models import load_model
from PIL import Image
import numpy as np
import tensorflow as tf
from .utils import get_plot


def index(request):
    return render(request, 'index.html')

# Create your views here.
def home(request):
    qs = AddPatient.objects.all()
    x = ["patient " + str(x.id) for x in qs]
    y = [y.tuberculosis for y in qs]
    c = [x.gender for x in qs]
    chart = get_plot(x, y)
    return render(request, 'home.html',context={"patients":qs, 'chart': chart})




def patient(request):
    if request.method == 'POST':
        nom = request.POST['First_Name']
        prenom = request.POST['Last_Name']
        date = request.POST['start_date']
        ville = request.POST['Ville']
        phone = request.POST['Mobile_Number']
        gender = request.POST['Gender']
        adresse = request.POST['Address']
        cin = request.POST['CIN']
        date_visite = request.POST['date_visite']
        image = request.FILES['image']
        path = os.path.join('media/images', image.name)
        with open(path, 'wb') as f:
            f.write(image.read())
        img = cv2.imread(path)
        image_name = image.name
        image_file = InMemoryUploadedFile(image, None, image_name, 'images/jpeg', image.size, None)

        # image_file2 = Image.open(image)
        image2 = cv2.resize(img, (96, 96))
        # Convert the image to a numpy array
        image_array = np.array(image2)

        # Normalize the pixel values to be between 0 and 1
        image_array = image_array / 255.0

        # Add an additional dimension to the image array
        image_array = np.expand_dims(image_array, axis=0)

        # Convert the numpy array to a TensorFlow tensor
        tensor = tf.convert_to_tensor(image_array)
        model = load_model("prediction/model.h5")
        prediction = model.predict(tensor)
        print(prediction)

        tuberculosis = "Normal"
        if prediction[0][1] >= 0.6:
            tuberculosis = "tuberculose"

        new_patient = AddPatient(nom=nom, prenom=prenom, date=date, ville=ville, phone=phone, gender=gender,
                                 adresse=adresse, cin=cin, date_visite=date_visite,
                                 image=image_file, tuberculosis=tuberculosis)
        new_patient.save()

        qs = AddPatient.objects.all()

        return render(request, 'home.html', context={"patient": new_patient, "patients":qs})

    return render(request, 'patient.html')
def patientView(request):
    qs = AddPatient.objects.all()
    x=["patient"+str(x.id) for x in qs]
    y=[y.tuberculosis for y in qs]
    chart = get_plot(x, y)
    return render(request, 'chartpie.html', {'chart': chart})
 # return render(request,'chartpie.html')




 # femme=AddPatient.objects.filter(gender='Female').count()
    # femme=int(femme)
    # homme = AddPatient.objects.filter(gender='Male').count()
    # homme = int(homme)
    # gender_list=['Male','Female']
    # gender_number=[homme,femme]
    # context={'gender_list':gender_list,'gender_number':gender_number}