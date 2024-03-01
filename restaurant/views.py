from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def IndexPageView(request):
    return render(request, 'users/index.html')

def TablePageView(request):
    return render(request, 'users/tables.html')

def menuPageView(request):
    return render(request, 'users/menu.html')

def stausfoodPageView(request):
    return render(request, 'users/food_status.html')

def siginPageView(request):
    return render(request, 'users/signin.html')

