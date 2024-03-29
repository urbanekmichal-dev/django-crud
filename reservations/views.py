from datetime import timezone, date, datetime

import django
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from reservations.forms import ReservationForms
from reservations.models import Reservations


# Create your views here.
def index(request):
    p = Paginator(Reservations.objects.all(), 8)
    page = request.GET.get('page')
    reservations = p.get_page(page)
    context = {'reservations': reservations}
    return render(request, 'reservations/indexadmin.html', context)


def delete(request, id):
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


# def roomDetails(request,id):
#     rooms = get_object_or_404(Room, id=id)
#     context = {'room': rooms}
#     return render(request, 'room/indexuser.html', context)

def view_my_reservations(request):
    if User.objects.filter(username=request.user):
        user = get_object_or_404(User, username=request.user)
        reservations = Reservations.objects.filter(user=user)

        for reservation in reservations:
            start_date = django.utils.timezone.now().date()
            end_date = reservation.end_date
            delta = end_date - start_date
            reservation.days_left = delta.days

        p = Paginator(reservations, 8)
        page = request.GET.get('page')
        reservations_list = p.get_page(page)
        context = {'reservations': reservations_list}
        return render(request, 'reservations/index.html', context)


def change_state(request, id):
    reservation_object = get_object_or_404(Reservations, id=id)
    if reservation_object.state == "Pending" and reservation_object.is_finished == False:
        reservation_object.state = "Ongoing"

    else:
        reservation_object.state = "Finished"
        reservation_object.book.is_available=True
        reservation_object.book.save()
    reservation_object.save()
    return redirect('view_reservations')
