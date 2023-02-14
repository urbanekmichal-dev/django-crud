from django.contrib.auth.models import User
from django.db import models

from book.models import Book


# Create your models here.

class Reservations(models.Model):
    ONGOING = 'Ongoing'
    PENDING = 'Pending'
    FINISHED = 'Finished'

    CHOICES = (
        (ONGOING, ONGOING),
        (PENDING, PENDING),
        (FINISHED, FINISHED),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    days_left = models.IntegerField()
    is_finished = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=255, choices=CHOICES, default=ONGOING)


