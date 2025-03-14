from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'authapp'

urlpatterns = [
    path('signup/', views.signupview, name= 'signup'),
    path('login/', views.loginview, name= 'login'),
    path('logout/', views.logoutview, name= 'logout'),
    path('settings/', views.settings_view, name= 'settings'),
    path('profile/', views.profile_view, name= 'profile'),
    path('settings/general/', views.edit_profile, name= 'profile_settings'),
    path('settings/password/', views.edit_password, name= 'password_settings'),
    path('settings/email/', views.edit_email, name= 'email_settings'),

]