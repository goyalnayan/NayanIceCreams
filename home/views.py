from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # whatever you will send from views will come at the place of {{variable}}
    context = {
        "variable1" : "Nayan is Intelligent",
        "variable2" : "Goyal is Nayan's Surname"
    }
    # remember you will have to render template in views.py not use HttpResponse 

    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")
    
def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    # for contact post request from contact.html it will store in a database 
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")
     