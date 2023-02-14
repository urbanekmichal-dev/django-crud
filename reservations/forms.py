from django.contrib.auth.models import User
from django.forms import  widgets, ModelForm

from book.models import Book
from reservations.models import Reservations

Book =[]
User =[]
class ReservationForms(ModelForm):
    class Meta:
        model = Reservations
        fields = ['book', 'start_date', 'end_date','user']
        widgets = {
            'book' : widgets.Select(choices=Book),
            'start_date': widgets.DateInput(attrs={'type': 'date'}),
            'end_date': widgets.DateInput(attrs={'type': 'date'}),
            'user' : widgets.Select(choices=User)
        }
