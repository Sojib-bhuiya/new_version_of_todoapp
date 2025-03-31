from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'media'

urlpatterns = [
    path('',views.media_list, name='media_list'), 
    path('upload/',views.media_upload, name='media_upload'),
    path('edit/<int:id>/',views.media_edit, name='edit_media'),
    path('delete/<int:id>/',views.media_delete, name='delete_media'),
]