from django.shortcuts import render

from user.models import User


def index(request):
    users = User.objects.order_by('-last_name')
    context = {'reservations': users}
    return render(request, 'user/index.html', context)