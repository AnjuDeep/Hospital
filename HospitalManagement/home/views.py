from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm
from .models import Contactenquiry
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)

def contact(request):
   
    return render(request,'contact.html')
def saveEnquiry(request):
        if request.method=="POST":
            enq_type=request.POST.get('enq_type')
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            country=request.POST.get('country')
            msg=request.POST.get('msg')
            en=Contactenquiry(enq_type=enq_type,c_name=name,c_email=email,c_phone=phone,c_address=address,c_country=country,c_message=msg)
            en.save()
        return render(request,'enquiry.html')

def anaesthesiology(request):
    return render(request,'anaesthesiology.html')
def checkup(request):
    return render(request,'checkup.html')
def insurance(request):
    return render(request,'insurance.html')
def careers(request):
    return render(request,'careers.html')
def treatment(request):
    return render(request,'treatment.html')
def openings(request):
    return render(request,'careers.html')

def breast(request):
    return render(request,'breast.html')
def cardiology(request):
    return render(request,'cardiology.html')
def gallery(request):
   
    return render(request,'gallery.html')
def critical(request):
    return render(request,'critical.html')
def dermatology(request):
    return render(request,'dermatology.html')
def emergency(request):
    return render(request,'emergency.html')
def ent(request):
    return render(request,'ent.html')
def nephrology(request):
    return render(request,'nephrology.html')
def neurology(request):
    return render(request,'neurology.html')
def ophthalmology(request):
    return render(request,'ophthalmology.html')
def paediatrics(request):
    return render(request,'paediatrics.html')
def urology(request):
    return render(request,'urology.html')

