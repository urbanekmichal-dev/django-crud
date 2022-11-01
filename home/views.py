from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from news.models import News


def index(request):
    return render(request, 'news.html')
