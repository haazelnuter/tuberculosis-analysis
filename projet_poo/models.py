from django.db import models

# Create your models here.
class AddPatient(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date = models.DateField(null=True)
    ville = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    GENDER_CHOICES = (
        ('Male', 'male'),
        ('Female', 'female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    adresse = models.TextField(max_length=50)
    cin = models.CharField(max_length=30)
    date_visite = models.DateField(null=True)
    image = models.ImageField(upload_to='images/', null=True)
    tuberculosis = models.TextField(max_length=50, null=True)


