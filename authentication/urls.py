from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import log_in, log_out, register_request

urlpatterns = [
    path('login/', log_in,name="login"),
    path('logout/', log_out, name="logout"),
    path('register/', register_request, name="register"),
]
