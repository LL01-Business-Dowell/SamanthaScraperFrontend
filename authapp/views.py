from django.shortcuts import render, redirect
from .forms import UserCreation, LoginForm, UserUpdate, PasswordChangeForm, EmailChange
from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.urls import reverse
from decouple import config

# Create your views here.

User = get_user_model()

#user singup view
def signupview(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authapp:login')
    else:
        form = UserCreation()
    return render(request, "signup.html", {"form": form})

#user login view
def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:home')

    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})    


#logout view
login_required()    
def logoutview(request):
    logout(request)
    return redirect('/home')

#view for editing basic user profile details
@login_required()
def settings_view(request):
    return render(request, 'settings.html')

@login_required()
def profile_view(request):
    return render(request, 'profile.html')

@login_required()
def edit_profile(request):
    form = UserUpdate(
            instance= request.user
        )
    if request.method == 'POST':
        form = UserUpdate(data= request.POST, instance= request.user)
        if form.is_valid():
            user = form.save()
            user.save()
            profile_url = reverse('authapp:profile', kwargs={"user_key": user.user_key})
            return redirect(profile_url)
        
    return render(request, "edit_profile.html", {"form": form})

def privacy_view(request):
    return render(request, 'privacy_settings.html')

#view for editing user password
@login_required()
def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('authapp:profile')
    else:
        form = PasswordChangeForm(request.user)
        
    return render(request, "edit_password.html", {"form": form})

#view for editing user email
@login_required()
def edit_email(request):
    user_object = User.objects.get(id= request.user.id)
    if request.method == 'POST':
        form = EmailChange(data= request.POST, instance= request.user)
        if form.is_valid():

            #extract password entered into form to check against current user password 
            password_entered = form.cleaned_data['confirm_password']
            if user_object.check_password(password_entered):
                user_object.email = form.cleaned_data['email']
                user_object.save()
                logout(request)
                return redirect('authapp:login')
            
            else:

                #if form is password entered is incorrect, raise an error
                form.add_error('confirm_password', 'Incorrect password. Please try again.')

    else:
        form = EmailChange(instance= request.user)
        
    return render(request, "edit_email.html", {"form": form})  
