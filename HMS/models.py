from django.db import models

# Create your models here.


class Reservation(models.Model):
 Room_number= models.CharField(max_length= 4)
 Amount_paid = models.CharField(max_length= 10)
 Occupant_name= models.CharField(max_length= 100)
 Occupant_email= models.EmailField() #with this fiel, the user/customer must provide a valid email format
 Occupant_Occupation= models.CharField(max_length= 50)
 Number_of_night= models.CharField(max_length=100)
 Start_date=models.CharField(max_length=100) #CharField was used because the DateField could not show when used
 End_date= models.CharField(max_length=100)
 def __str__(self):     #this helps to ensure that the new user saved is saving in the same name as the Occupant
     return self.Occupant_name