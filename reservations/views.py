from datetime import timezone

from django.shortcuts import render, get_object_or_404, redirect

from reservations.forms import ReservationForms
from reservations.models import Reservations


# Create your views here.
def index(request):
    reservations = Reservations.objects.order_by('-name')
    context = {'reservations': reservations}
    return render(request, 'reservations/index.html', context)

def delete(request,id):
    news_object = get_object_or_404(Reservations, id=id)
    news_object.delete()
    return redirect("view_reservations")

def add(request):
    if request.method == 'POST':
        reservation = ReservationForms(request.POST)
        if reservation.is_valid():
            reservations = reservation.save(commit=False)
            reservations.save()
            return redirect('view_reservations')
        else:
            context = {'form': reservation, 'edit': False}
            return render(request, 'reservations/add.html', context)


    else:
        news = ReservationForms()
        context = {'form': news}
        return render(request, 'reservations/add.html', context)

def edit(request, id):
    reservation_object = get_object_or_404(Reservations, id=id)
    reservations = ReservationForms(instance=reservation_object)
    context = {'form': reservations, 'id': id, 'edit': True}
    return render(request, 'reservations/add.html', context)

def update(request, id):
    reservations = ReservationForms(request.POST)
    if reservations.is_valid():
        reservation = reservations.save(commit=False)

        reservation.save()
        reservation_object = get_object_or_404(Reservations, id=id)
        reservation_object.delete()
        return redirect('view_reservations')
    else:
        return edit(request, id)