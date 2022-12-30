from django import forms
from .models import Book
from django.forms import  widgets, ModelForm
import datetime


# class NewsForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = ['topic', 'text', 'author']

class BookForms(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'publisher', 'published','image','description','category']
        widgets = {
            'published': widgets.DateInput(attrs={'type': 'date'}),

        }


