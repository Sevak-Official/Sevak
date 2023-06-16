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
#abc-user
#aaaa@332-password
#user-AJIMS
#pass-123@aaAb
#user-BJIMS
#pass-123@abc
#user-JJIMS
#pass-123@Aabc
def about(request):
     features = [
        {
            'title': 'Advanced Search & Filter',
            'points': [
                    "Detailed search functionality for patients",
                    "Precise Specialization-based Filtering",
                    "Effortless, User-friendly Interface"
                ],
        },
        {
            'title': 'Detailed Facility Information',
            'points': [
                    "Explore clinics and hospitals for treatment",
                    "Multiple options: hospitals and clinics",
                    "Detailed info on healthcare facilities"
                ],
        },
        {
            'title': 'Hospital Partnership',
            'points': [
                    "Register, share information",
                    "Strengthening local physician search",
                    "Comprehensive care provision"
                ],
        },
        {
            'title': 'Secure Access',
            'points': [
                    "Restricted access for authenticated users",
                    "Secure information management",
                    "No External Editing"
                ],
        },
    ]
     business_models = [
        {
            'title': 'Freemium',
            'description': 'The app could be offered for free, with users paying for additional premium features such as more detailed search results or the ability to book appointments directly through the app.',
        },
        {
            'title': 'Subscription-based',
            'description': 'Under this model, users would pay a recurring fee in order to access certain features of the app, such as the ability to search for medical professionals and treatment options.',
        },
        {
            'title': 'Advertising',
            'description': 'Healthcare providers could pay to advertise their services on the app through sponsored search results or banner ads.',
        },
        {
            'title': 'Commission-based',
            'description': 'The app could take a percentage of the fees charged by the medical professionals and hospitals listed on the platform, similar to how online travel agencies function.',
        },
        {
            'title': 'Hybrid',
            'description': 'This model could combine elements of multiple business models, such as offering a basic version for free while charging for premium features and/or allowing healthcare providers to advertise on the platform.',
        },
    ]
    
     context = {'features': features,'business_models':business_models}
     return render(request,'hck/hospital/about.html',context)
def base(request):
    return render(request,'hck/base.html')
@login_required(login_url='/login')
def main(request):
    if request.method=="POST":
     form=DoctorForm(request.POST)
     if form.is_valid():
        specialization=request.POST['specialization']
        name=request.POST['name']
        city=request.POST['city']
        t=form.save(commit=False)
        t.user = request.user
        t.save()
    else:
         form=DoctorForm()
    table = Doctor.objects.all()
    paginator = Paginator(table, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'hck/hospital/hospitals.html', {
        "form": form,
        "table": table,
        "page_obj": page_obj
    })
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
            return redirect('login')
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
