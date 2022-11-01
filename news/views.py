from django.shortcuts import render

# Create your views here.
def get_news(request):
    return render(request, "news.html")