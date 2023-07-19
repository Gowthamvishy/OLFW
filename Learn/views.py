from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages

def Home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        cpass = request.POST['cpass']
        print(fname,lname)
        if User.objects.filter(username=email).exists():
            messages.error(request,"Username already exists!")
        elif fname=='' or lname=='' or email=='' or pass1=='' or cpass == '':
            messages.error(request,"Fields should not be empty!")
        elif pass1 != cpass:
            messages.error(request,"Confirm password doesn't match!")
        else:
            User.objects.create_user(email=email,first_name=fname,last_name=lname,username=email,password=pass1)
            messages.success(request,"Successfully Created go to login page!")


    return render(request,'signup.html')

def signin(request):
    username = request.POST['email']
    password = request.POST['pass']
    user = authenticate(request, username=username, password=password)
    if username == "" or password == "":
        messages.error(request,"Fields should not be empty!")
        return render(request,'index.html')
    elif user is not None:
        return render(request,'homepage.html')
    else:
        messages.error(request,"Username or password is wrong!")
        return render(request,'index.html')