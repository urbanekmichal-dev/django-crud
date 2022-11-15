from django.db import models

# Create your models here.
class Reservations(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    room = models.CharField(max_length=200)
    check_in = models.DateField()
    check_out = models.DateField()