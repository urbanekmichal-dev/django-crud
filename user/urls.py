from django.urls import path

from user.views import index

urlpatterns = [
    path('', index, name='view_users'),

]