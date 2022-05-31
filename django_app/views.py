from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def users(request):
    # return HttpResponse('Users')
    return render(request, 'users.html')

def home(request):
    # return HttpResponse('Users')
    return render(request, 'home.html')
