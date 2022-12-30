import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from book.forms import BookForms
from book.models import Book
from reservations.forms import ReservationForms
from reservations.models import Reservations
from reservations.utilities import calc_days_left


# Create your views here.

def index(request):
    p = Paginator(Book.objects.all(), 8)
    page = request.GET.get('page')
    books_list = p.get_page(page)

    context = {"books_list" : books_list}
    return render(request, 'book/index.html', context)

def indexuser(request):

    available_books=Book.objects.filter(is_available=True)
    p = Paginator(available_books, 8)
    page = request.GET.get('page')
    books_list = p.get_page(page)

    context = {"books_list" : books_list}
    return render(request, 'book/indexuser.html', context)


@login_required(login_url='/login/')
def add(request):
    if request.method == 'POST':
        form = BookForms(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Added successful")
            return redirect('view_books')

        else:
            context = {'form': form}
            messages.error(request, "Invalid information.")
            return render(request, 'book/add.html', context)

    else:
        news = BookForms()
        context = {'form': news}
        return render(request, 'book/add.html', context)



def get(request, id):
    news = get_object_or_404(Book, id=id)
    context = {'book': news}
    return render(request, 'book/view.html', context)

def edit(request, id):
    news_object = get_object_or_404(Book, id=id)
    news = BookForms(instance=news_object)
    context = {'form': news, 'id': id}
    return render(request, 'book/edit.html', context)

def update(request, id):
    book = BookForms(request.POST)
    if book.is_valid():
        book = book.save(commit=False)
        book.create_time = timezone.now()
        book.last_edit_time = timezone.now()
        book.save()
        book_object = get_object_or_404(Book, id=id)
        book_object.delete()
        return redirect('view_books')
    else:
        return edit(request, id)

def delete(request,id):
    book_object = get_object_or_404(Book, id=id)
    messages.success(request, 'Book - {} Deleted succesfully '.format(book_object.name))
    book_object.delete()
    return redirect("view_books")

def reserve_book(request,id):
    book =get_object_or_404(Book, id=id)
    book.is_available=False
    book.save()
    start_date= timezone.now()
    end_date=timezone.now() + datetime.timedelta(days=15)
    user=get_object_or_404(User, id=1)
    user = get_object_or_404(User, username=request.user)
    reservation = Reservations.objects.get_or_create(book=book, start_date=start_date,end_date=end_date,user=user,days_left=calc_days_left(start_date,end_date),is_finished=False)
    return redirect("view_books")

def return_book(request,id):
    reservation = get_object_or_404(Reservations, id=id)
    reservation.is_finished=True
    reservation.save()
    reservation.book.is_available=True
    reservation.save()
    reservation.book.save()

    return redirect("view_books")


