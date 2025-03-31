from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('login/', auth_views.LoginView.as_view(template_name='todoapp/loging.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    # path('logout/', views.logoutPage, name='logout'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete'),
    path('edit_task/<int:pk>/', views.update_task, name='edit_task'),
]

# Eg>k<1~773lT