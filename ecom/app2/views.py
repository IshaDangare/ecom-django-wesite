from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User #import user
from django.contrib.auth import authenticate,login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        uname=request.POST['username']
        fname = request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            myuser=User.objects.create_user(username=uname,password=password1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.email=email
            myuser.save()
            return redirect('Login')
        else:
            return HttpResponse("Enter same Password as password")
        #create user
        # print(uname,fname,lname,email,password1)
        
        # firstname=fname,lastname=lname,
    else:
        return render(request,'auth/signup.html')
        
def Login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        password1=request.POST['password1']
        user=authenticate(request,username=uname,password=password1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("Uersname or Password is incorrect!!")
            # popup="Uersname or Password is incorrect!!"
    return render(request,'auth/Login.html')


    