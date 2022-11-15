from django.urls import path, include
from .views import index, add, get, edit, update

urlpatterns = [
    path('', index, name='view_news'),
    path('add/', add, name='add_news'),
    path('<int:id>/', get, name='get_news'),
    path('edit/<int:id>/', edit, name='edit_news'),
    path('update/<int:id>/', update, name='update_news')
]
