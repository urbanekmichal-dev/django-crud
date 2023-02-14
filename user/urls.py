from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from user.views import view_user_profile, view_all_users, view_user_profile_id,update_user,user_details_admin,change_user_state

urlpatterns = [
    path('user/', view_user_profile, name='view_user_profile'),
    path('', view_all_users, name='view_all_users'),
    path('user/<int:id>/', view_user_profile_id,name="view_user_profile_id"),
    path('update/<int:id>/', update_user, name="update_user"),
    path('userDetailsAdmin/<int:id>/', user_details_admin, name="user_details_admin"),
    path('changeUserState/<int:id>/', change_user_state, name="change_user_state"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)