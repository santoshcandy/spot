# booking/forms.py

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['Phone', 'Name', 'Location', 'services', 'Datetime', 'Message']
