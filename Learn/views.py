from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
            return HttpResponse("<h1>Email already exists!</h1>")
        elif fname=='' or lname=='' or email=='' or pass1=='' or cpass == '':
            return HttpResponse("<h1>Fields Should not be Empty!</h1>")
        elif pass1 != cpass:
            return render(request, 'password.html')
        else:
            User.objects.create_user(email=email,first_name=fname,last_name=lname,username=email,password=pass1)
            return render(request,'signsuccess.html')


    return render(request,'signup.html')

def signin(request):
    username = request.POST['email']
    password = request.POST['pass']
    user = authenticate(request, username=username, password=password)
    if user is not None:
            login(request, user)
            return render(request,'login.html')
    else:
        return render(request, 'wronglog.html')


