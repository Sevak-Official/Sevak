from django.shortcuts import render,redirect
from .forms import RegisterForm,DoctorForm,PatientForm
from .models import Hospital,Doctor,Patient
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
# Create your views here.
# team-superuser
# team404-pass
# team1-user
# team404@-pass
# team-user
# team404@1-pass
#abc-user
#aaaa@332-password
def about(request):
    return render(request,'hck/hospital/about.html')
def base(request):
    return render(request,'hck/base.html')
@login_required(login_url='/login')
def main(request):
    table=Doctor.objects.all()
    paginator = Paginator(table, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method=="POST":
     form=DoctorForm(request.POST)
     if form.is_valid():
        specialization=request.POST['specialization']
        name=request.POST['name']
        city=request.POST['city']
        t=form.save(commit=False)
        t.user = request.user
        t.save()
        return render(request,'hck/hospital/hospitals.html',{"table":table,"page_obj":page_obj})
    else:
         form=DoctorForm()
    return render(request,'hck/hospital/hospitals.html',{"form":form,"table":table,"page_obj":page_obj})
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.user=request.user
            p.save()
            date_established = form.cleaned_data.get('date_established')
            city = form.cleaned_data.get('city')
            pincode = form.cleaned_data.get('pincode')
            address = form.cleaned_data.get('address')
            website = form.cleaned_data.get('website')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.get(username=username)
            user_data = Hospital.objects.create(user=user,date_established=date_established,city=city,pincode=pincode,
             address=address,website=website,email=email)
            user_data.save()
            k= authenticate(username=username, password=password)
            login(request, k)
            return render(request, 'registration/login.html', {'form': form})
    else:
         form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})
def patients(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q=Q(Q(city__icontains=q) | Q(specialization__icontains=q) | Q(name__icontains=q)) 
        table = Doctor.objects.filter(multiple_q)
    else:
        table = Doctor.objects.all()
    paginator = Paginator(table, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method=="POST":
     form=PatientForm(request.POST)
     if form.is_valid():
        city=request.POST['city']
        symptoms=request.POST['symptoms']
        form.save(commit=False)
        user_data = Patient.objects.create(city=city,symptoms=symptoms)
        user_data.save() 
        return render(request, 'hck/patient/patients.html',{"table":table,"page_obj":page_obj})
    else:
         form=PatientForm()
    return render(request,'hck/patient/patients.html',{"form":form,"table":table,"page_obj":page_obj})
