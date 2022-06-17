from django.urls import path
from .views import index, about, contact, services

urlpatterns = [
    path('', index),
    path('about-us/', about),
    path('contact-us/', contact),
    path('services', services)
    
    ]



