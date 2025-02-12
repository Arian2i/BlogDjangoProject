from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'accounts_app/login.html', context={})