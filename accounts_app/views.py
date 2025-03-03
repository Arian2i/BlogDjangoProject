from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')  # if user loge in dont show them login page
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)  # if user Auth print name else print None
        if user is not None:
            login(request, user)
            return redirect('home_app:home')
    return render(request, 'accounts_app/login.html', context={})


def user_logout(request):
    logout(request)
    return redirect('home_app:home')


def user_register(request):
    context = {"errors": []}
    if request.user.is_authenticated:
        return redirect('home_app:home')  # if user logged in, don't show them the login page
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

            # Authenticate the user and log them in
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                return redirect('home_app:home')
            else:
                context["errors"].append("Error in registration")
                return render(request, 'accounts_app/register.html', context)
        else:
            context["errors"].append('Passwords do not match')
            return render(request, 'accounts_app/register.html', context)
    else:
        return render(request, 'accounts_app/register.html', context={})
