from django.shortcuts import render
from app1.models import Doctor, Patient
from app1.serializers import DoctorSerializer, PatientSerializer    
from rest_framework import viewsets   
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

def home(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    context = {
        'doctors': doctors,
        'patients': patients
    }

    return render(request, 'app1/home.html', context)



class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]


class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
