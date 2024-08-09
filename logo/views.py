from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Register
# Create your views here.
def signin(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["password"] 
        user=Register.objects.filter(username=username,password=password).first()
        if user is None:
            messages.error(request,'Invalid password')
            return redirect('signin')
        else:
            request.session['uname']=username
            return redirect('home')
    return render(request,"signin.html")  
def register(request):
    if request.method=="POST":
        name=request.POST["name"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        username=request.POST["uname"]
        password=request.POST["password"]
        myreg=Register(name=name,phone=phone,email=email,username=username,password=password)
        myreg.save()
        return redirect('signin')
    return render(request,"register.html")
def logout(request):
    if 'uname' in request.session:
        request.session.flush()
        return redirect('signin')
def index(request):
    if 'uname' not in request.session:
        return request('signin')
    return render(request,"indexnew.html")
def viewall(request):
    if 'uname' not in request.session:
        request.session.flush()
        return redirect('signin')
    reg=Register.objects.all()
    context={
        'reg':reg
    }
    return render(request,"viewreg.html",context)
def updatereg(request,pk):
    reg=Register.objects.get(id=pk)
    dic={
        'reg':reg
    }
    return render(request,"register.html",dic)
def updatedata(request,pk):
    name=request.POST["name"]
    phone=request.POST["phone"]
    email=request.POST["email"]
    username=request.POST["uname"]
    password=request.POST["password"]
    reg= Register.objects.get(id=pk)
    reg.name=name
    reg.phone=phone
    reg.email=email
    reg.username=username
    reg.password=password
    reg.save()
    return HttpResponseRedirect(reverse('viewall'))
