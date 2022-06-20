from django.shortcuts import redirect, render
from .forms import ReservationForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, 'HMS/index.html', {"INTRO": "WELCOME TO XYZ HOTEL, WEBSITE STILL UNDER CONSTRUCTION"}) 

def about(request):
    return render(request, 'HMS/about.html', {'ABOUT':'AT XYZ, WE ENSURE YOU FEEL AT HOME'})

def contact(request):
    return render(request, 'HMS/contact.html', {'contact':'FEEL FREE TO REACH US 24/7'})

def services(request):
    return render(request, 'HMS/services.html', {'services':'WE RENDER GENUINE SERVICES EVEN AT ODD HOURS'})

def create_reservation_view(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(index)
    #context['form']= ReservationForm()
    return render(request, 'HMS/create_reservation.html', {'form':UserCreationForm})