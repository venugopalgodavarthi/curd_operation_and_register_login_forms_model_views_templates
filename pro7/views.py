from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from pro7.forms import registerform
from authe.models import registermodel

def welcome(request):
    return render(request,'welcome.html')

def sample(request):
    print(request)
    if request.method=='POST':
        res=request.POST['username']
        res1=request.POST['password']
        print(res,res1)
        print(request.POST)
        print(type(request.POST))
    return render(request,'sample.html')


def register(request):
    if request.method=='POST':
        user=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['repassword']
        email=request.POST['email']
        phone=request.POST['phone']
        dob=request.POST['dob']
        gender=request.POST['gender']        
        print(user,pass1,pass2,email,phone,dob,gender,)
        if pass1==pass2:
            registermodel.objects.create(username=user,password=pass2,email=email,gender=gender,dob=dob,phone=phone)
            return redirect('login')
        else:
            return HttpResponse('password is incorrect')
    form=registerform()
    return render(request,'register.html',{'form':form})

def details(request):
    res=registermodel.objects.all()
    return render(request,'details.html',{'res':res})

def sdetails(request):
    res=False
    if request.method=='POST':
        email=request.POST['email']
        res= registermodel.objects.filter(email=email)
    form=registerform()
    return render(request,'sdetails.html',{'form':form,'res':res})

def update(request,email):
    if request.method=='POST':
        user=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['repassword']
        email=request.POST['email']
        phone=request.POST['phone']
        dob=request.POST['dob']
        gender=request.POST['gender']        
        print(user,pass1,pass2,email,phone,dob,gender,)
        if pass1==pass2:
            registermodel.objects.filter(email=email).update(username=user,password=pass2,email=email,gender=gender,dob=dob,phone=phone)
            return HttpResponse('data is updated')
        else:
            return HttpResponse('password is incorrect ')
    res=registermodel.objects.get(email=email)
    return render(request,'update.html',{'res':res})

def delete(request,email):
    if request.method=='POST':
        registermodel.objects.filter(email=email).delete()
        return HttpResponse('data is deleted')
    res=registermodel.objects.get(email=email)
    return render(request,'delete.html',{'res':res})
    
    
def login(request):
    if request.method=='POST':
        user=request.POST['username']
        pass1=request.POST['password'] 
        print(user,pass1)
        res=registermodel.objects.all()
        for i in res:
            if user==i.email:
                if pass1==i.password:
                    return render(request,'home.html',{'user':i.username})
        else:
            return HttpResponse('username  or password is incorrect ')
    form=registerform()
    return render(request,'login.html',{'form':form})

def home(request):
    user='UNKNOWN PERSON'
    return render(request,'home.html',{'user':user})


def logout(request):
    return render(request,'welcome.html')