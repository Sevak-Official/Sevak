from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doctor,Patient

class RegisterForm(UserCreationForm):
    city = forms.CharField(max_length=100,label="City")
    date_established = forms.DateField(label="Date Established")
    pincode = forms.CharField(max_length=6, label="Pincode")
    address=forms.CharField(max_length=200)
    website=forms.URLField(label="Your Website", required=False)
    email=forms.EmailField(label="Email",required=True)
    username=forms.CharField(label="Hospital Name")
    class Meta:
        model = User
        fields = ["username", "password1", "password2","website","date_established","city","address","pincode","email"]

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=["specialization","name","city","clinic_website"]
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=["city","symptoms"]