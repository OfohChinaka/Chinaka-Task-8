# from django, import the forms
from django import forms

# import Reservation model from the model.py section
from .models import Reservation

#develop a ModelForm class
class ReservationForm(forms.ModelForm):
    # specify model name to create form
    class Meta:
        model = Reservation
        fields = "__all__"