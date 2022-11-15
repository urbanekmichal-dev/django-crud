from django.db import models

# Create your models here.

class Room(models.Model):
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=100)
    floor = models.IntegerField()

class Reservations(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()


