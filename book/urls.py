from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import index, add, get, edit, update, delete, indexuser, reserve_book,return_book,change_visibility

urlpatterns = [
    path('', index, name='view_books'),
    path('userview/', indexuser, name='view_books_user'),
    path('add/', add, name='add_book'),
    path('<int:id>/', get, name='get_book'),
    path('edit/<int:id>/', edit, name='edit_book'),
    path('update/<int:id>/', update, name='update_book'),
    path('delete/<int:id>/', delete, name='delete_book'),
    path('reserve/<int:id>/', reserve_book, name='reserve_book'),
    path('return/<int:id>/', return_book, name='return_book'),
    path('changeVisibility/<int:id>/', change_visibility, name='change_visibility')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)