from django.urls import path, include

from reservations.views import index, delete, add, edit, update, roomDetails

urlpatterns = [
    path('', index, name='view_reservations'),
    path('add/', add, name='add_reservation'),
    path('edit/<int:id>/', edit, name='edit_reservation'),
    path('update/<int:id>/', update, name='update_reservation'),
    path('delete/<int:id>/', delete, name='delete_reservation'),
    path('roomDetails/<int:id>/', roomDetails, name='room_details')

]
