from django.urls import path
from .views import index, about, contact, services, create_reservation_view
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('about-us/', about),
    path('contact-us/', contact),
    path('services/', services),
    path('create_reservation/', views.create_reservation_view, name= 'create-reservation'),
    
    ]



