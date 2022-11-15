from django.forms import  widgets, ModelForm

from reservations.models import Reservations


class ReservationForms(ModelForm):
    class Meta:
        model = Reservations
        fields = ['name', 'surname', 'room','check_in',"check_out"]
        widgets = {
            'room' : widgets.NumberInput(attrs = {'maxlength': 3}),
            'check_in': widgets.DateInput(attrs={'type': 'date'}),
            'check_out': widgets.DateInput(attrs={'type': 'date'}),
        }