from django.contrib import admin
from .models import Reservation

# Register your models here.
#the hotel management can input the details via the admin log in page


admin.site.register(Reservation) #we need to register the model name here to ensure it shows in the admin web section
