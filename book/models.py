from django.db import models

# Create your models here.


# class News(models.Model):
#     topic = models.CharField(max_length=100)
#     text = models.CharField(max_length=200)
#     author = models.CharField(max_length=200)
#     create_time = models.DateTimeField('create time')
#     last_edit_time = models.DateTimeField('last edit time')

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    published = models.DateField()
    category = models.CharField(max_length=100)
    is_available=models.BooleanField(default=True)
    description=models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/')