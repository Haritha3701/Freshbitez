from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import auth,User

# Create your views here.
def test(request):
    return render(request,"test.html")

def index(request):
    return render(request,"index.html")

def login(request):
    if request.method=="POST":
        usern=request.POST["uname"]
        pswd=request.POST["pwd"]
        user=auth.authenticate(username=usern,password=pswd)
        if user is not None:
            auth.login(request,user)
            msg="Login Successful"
            return redirect("/")
        else:
            msg="Invalid username and password"
            return render(request,"login.html",{"msg":msg})
    
    else:
        return render(request,"login.html")

    
    

def register(request):
    if request.method=="POST":
        firstname=request.POST["fname"]
        lastname=request.POST["lname"]
        usern=request.POST["uname"]
        email=request.POST["emailid"]
        pwsd=request.POST["pwd"]
        rpwsd=request.POST["repwd"]

        if pwsd==rpwsd:
            if User.objects.filter(username=usern).exists():
                msg="Username is already taken"
            elif User.objects.filter(email=email).exists():
                msg="Email already taken"
            else:
                user=User.objects.create_user(username=usern,first_name=firstname,last_name=lastname,email=email,password=pwsd)
                user.save();
                msg="Registration successful"
                return redirect("loginpage")
                
        else:
            msg="Password and repassword are not same"
            return render(request,"register.html",{"msg":msg})
        
    else:                           
        return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect("/")