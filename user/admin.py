from django.contrib import admin

from user.models import CustomUser

# from user.models import User

# Register your models here.
admin.site.register(CustomUser)