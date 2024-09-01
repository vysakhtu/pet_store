from django.shortcuts import render,redirect
from .models import Pet
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import signupform
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def list_pets(request):
    object_list=Pet.objects.all()
    return render(request,'petsapp/list_pets.html',
    {'object_list':object_list})

def pet_detail(request,id):
    idd=Pet.objects.get(id=id)
    return render(request,'petsapp/petdetail.html',
    {'data':idd})

def register(request):
    if request.method=='POST':
        fn=signupform(request.POST)
        if fn.is_valid():
            uname=fn.cleaned_data['username']
            upass=fn.cleaned_data['password1']
            print(uname)
            print(upass)
            fn.save()
            return redirect("/login")
    else:
        fn=signupform()
    return render(request,'petsapp/signup.html',{'form':fn})           

def signup(request):
    if request.method=='POST':
        fn=signupform(request.POST)
        if fn.is_valid():
            uname=fn.cleaned_data['username']
            upass=fn.cleaned_data['password1']
            print(uname)
            print(upass)
            fn.save()
            return redirect("/login")
        else:
            fn=signupform()
        return render(request,'petsapp/signup.html',{'form':fn})           


def user_login(request):
    if request.method=='POST':
        fn=AuthenticationForm(request=request,data=request.POST)
        if fn.is_valid():
            uname=fn.cleaned_data['username']
            upass=fn.cleaned_data['password']
            u=authenticate(username=uname,password=upass)
            print(u)
            return redirect('/list_pets')
    else:
        fn=AuthenticationForm()
    return render(request,'petsapp/login.html',{'form':fn})
def profile(request):
    return render(request,'petsapp/list_pets.html')
def user_logout(request):
    return redirect('/login')

