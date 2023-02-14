from django.forms import ModelForm
from django.forms import  widgets, ModelForm
from user.models import CustomUser


class UserForms(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone', 'street','city','state','zip_code','image']
