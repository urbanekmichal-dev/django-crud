from django.urls import path, include

from reservations.views import index, delete, add, edit, update,view_my_reservations

urlpatterns = [
    path('', index, name='view_reservations'),
    path('view_reservations_user/', view_my_reservations, name='view_reservations_user'),
    path('add/', add, name='add_reservation'),
    path('edit/<int:id>/', edit, name='edit_reservation'),
    path('update/<int:id>/', update, name='update_reservation'),
    path('delete/<int:id>/', delete, name='delete_reservation'),

]
