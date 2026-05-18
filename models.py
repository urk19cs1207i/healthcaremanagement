from django.db import models

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    def __str__(self):
        return self.name

class Patient(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    city=models.CharField(max_length=100)
    treatment=models.CharField(max_length=100)
    consult_doctor=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    def __str__(self):
        return self.name