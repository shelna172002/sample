from django.shortcuts import render, HttpResponse
from .models import Department,Doctor
from .forms import BookingForm


# Create your views here.
def index(request):
    #return HttpResponse("hello welcome")
    person={
        'name' : 'Shelna',
        'age' : 12,
        'place' : 'Thiroor',
    }
    return render(request,"index.html",person)
def about(request):
    #return HttpResponse("About us")
    return render(request,"about.html",{'range': range(1,11)})
def show(request):
    number1={
        'num':[1,2,3,4,5,6,7,8,9]
    }
    return render(request,"show.html",number1)


def department(request):
    dic_dept={
        'dept':Department.objects.all()
    }
    return render(request,"department.html",dic_dept)

def doctor(request):
    dic_doc={
        'doc':Doctor.objects.all()
    }
    return render(request,"doctor.html",dic_doc)

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form=BookingForm()
        dic_form={
        'form':form
    }
    return render(request,"booking.html",dic_form)