from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {"variable": "this is sent"}
    return render(request, "index.html", context)
    # return HttpResponse("here's Home Page")

def about(request):
    # return HttpResponse("About here")
    return render(request, "about.html")
def services(request):
    # return HttpResponse("service")
    return render(request, "services.html")


def contact(request):
    # return HttpResponse("Contact Us")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent :)')
    return render(request, 'contact.html')


