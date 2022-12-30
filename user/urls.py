from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from user.views import view_user_profile, view_all_users, view_user_profile_id,update_user

urlpatterns = [
    path('user/', view_user_profile, name='view_user_profile'),
    path('', view_all_users, name='view_all_users'),
    path('user/<int:id>/', view_user_profile_id,name="view_user_profile_id"),
    path('update/<int:id>/', update_user, name="update_user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)