from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'HMS/index.html', {"INTRO": "WELCOME TO XYZ HOTEL, WEBSITE STILL UNDER CONSTRUCTION"}) 

def about(request):
    return render(request, 'HMS/about.html', {'ABOUT':'AT XYZ, WE ENSURE YOU FEEL AT HOME'})

def contact(request):
    return render(request, 'HMS/contact.html', {'contact':'FEEL FREE TO REACH US 24/7'})

def services(request):
    return render(request, 'HMS/services.html', {'services':'WE RENDER GENUINE SERVICES EVEN AT ODD HOURS'})
