from django.contrib.auth.models import User
from django.db import models

from book.models import Book


# Create your models here.

# class Room(models.Model):
#     room_number = models.IntegerField()
#     room_type = models.CharField(max_length=100)
#     floor = models.IntegerField()

class Reservations(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    days_left = models.IntegerField()
    is_finished=models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


