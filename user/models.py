from django.contrib.auth.models import User
from django.db import models

class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
