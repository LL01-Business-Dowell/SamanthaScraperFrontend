from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name= 'home'),
    path('notifications/', views.notification_view, name= 'notifications'),
    path('tasks/', views.processes_view, name= 'tasks'),
    path('tasks/<str:file_id>/', views.task_view, name= 'task_file'),
]