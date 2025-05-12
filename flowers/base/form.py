from django import forms
from .models import contactform,Order,BookingForm

class contactform(forms.ModelForm):
    class Meta:
       model=contactform
       fields=['firstname','email','phone',]

class Order(forms.ModelForm):
    class Meta:
     model=Order
     fields=['orderid','ocassion']

class BookingForm(forms.ModelForm):
    class Meta:
     model=BookingForm
     fields=['bookingnumber','firstname','lastname']

