from django.urls import path
from .views import main,sign_up,base,patients,about,doctors,login

urlpatterns = [
    path('',base,name='base'),
    path('patients/',patients,name='patients'),
    path('hospitals/',main,name='main'),
    path('sign-up/',sign_up,name='sign_up'),
    path('about/',about,name='about'),
    path('doctors/',doctors,name='doctors'),
]