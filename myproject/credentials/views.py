from django.shortcuts import render,redirect
#from Description.models import inform
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
   
    if request.method=="POST": 
        password=request.POST["pwd"]
        username=request.POST["uname"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"you are loged in")
            return redirect('/')
        else:
            messages.info(request,"No such User")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
def register(request):

    if request.method=="POST":

         first_name=request.POST["fname"]
         last_name=request.POST["lname"]
         email=request.POST["email"]
         password=request.POST["pwd"]
         username=request.POST["uname"]

         if(username=='' or first_name=='' or last_name=='' or email=='' or password==''):
                messages.info(request,"Required Field")
                return render(request,"register.html")
                #return render(request,"home.html",{'dlists':dlists})
         else:
                user=User.objects.create_user(first_name=first_name,
                last_name=last_name,email=email,password=password,
                username=username
                                )      
        
                user.save()
                messages.info(request,"User Registered Successfully!")
                #return render(request,"register.html")
                return redirect('/')
                #messages.info(request,"")
                #print("One record Inserted!")
    else:
     return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
    #messages.info(request,"logout")
