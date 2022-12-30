from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Hospital(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_established = models.DateField(null=True,blank=False)
    city = models.CharField(max_length=100,null=True,blank=False)
    pincode = models.CharField(max_length=6,null=True,blank=False)
    address=models.CharField(max_length=200,null=True,blank=False)
    website=models.URLField(null=True,blank=False)
    email=models.EmailField(null=True,blank=False)
    def __str__(self):
        return  f"{self.city} {self.email} "
    
class Doctor(Hospital):    
       SOME_CHOICES = (
  ("SELECT","SELECT"),
    ( "Gastroenterology","Gastroenterology(Discomfort in stomach,Digestive Disorders)"),
    ("Cardiography","Cardiography(Chest Pain)"),
    ("Radiology","Radiology(X-Ray)"),
    ("Orthopedics","Orthopedics(Injury,Fracture)"),
    ("Opthalmology","Opthalmology(Problem in Eyes)"),
    ("Psychiatry","Psychiatry(Depression,Mental Health)"),
    ("Dermatology","Dermatology(Skin Problem)"),
    ("Otolaryngologist","Otolaryngologist(Ear,Nose or Throat Issues)"),
    ("Nephrology","Nephrology(Kidney Disease)"),
    ("Dentist","Dentist(ToothCheck)"),
)      
       specialization=models.CharField(max_length=200,choices=SOME_CHOICES,default="--")
       name=models.CharField(max_length=100)
       clinic_website=models.URLField(null=True,blank=False)
       def __str__(self):
        return  f"{self.specialization} {self.name} "
class Patient(models.Model):
    D_CHOICES = (
      ("SELECT","SELECT"),
    ("Discomfort in stomach,Digestive Disorders", "Discomfort in stomach,Digestive Disorders"),
    ("Chest Pain", "Chest Pain"),
    ("X-Ray", "X-Ray"),
    ("Injury,Fracture", "Injury,Fracture"),
    ("Problem in Eyes","Problem in Eyes"),
    ("Depression,Mental Health","Depression,Mental Health"),
    ("Skin Problem","Skin Problem"),
    ("Ear,Nose or Throat Issues","Ear,Nose or Throat Issues"),
    ("Kidney Disease","Kidney Disease"),
    ("ToothCheck","ToothCheck")
)   
    
    city = models.CharField(max_length=100,null=True,blank=False)
    symptoms=models.CharField(max_length=60,choices=D_CHOICES,default="SELECT")
    def __str__(self):
        return  f"{self.symptoms} {self.city} "