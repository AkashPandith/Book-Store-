from django.shortcuts import render,HttpResponse, redirect
from datetime import datetime
from Book.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, "index.html")
#    return HttpResponse("This is the HOME Page")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name=name,email=email,message=message, date = datetime.today())
        contact.save()
        messages.success(request, "Your Message has been sent")
    return render(request, "contact.html")

def store(request):
    return render(request, "store.html")

def rent(request):
    return render(request, "rent.html")



# password for hte sky user - Sky@123456
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/home")
        else:
            # No backend authenticated the credentials
            return render(request, "login.html")

    return render(request, "login.html")