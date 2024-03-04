from django.shortcuts import render
from django.http import HttpResponse
from .models import Table,Menu
# Create your views here.



def IndexPageView(request):
    return render(request, 'users/index.html')

def TablePageView(request):
    tables = Table.objects.all().values()
    context = {
    'tables': tables,
  }
    return render(request, 'users/tables.html',context)

def menuPageView(request):
    menu = Menu.objects.all().values()
    context = {
    'menu': menu,
  }
    return render(request, 'users/menu.html',context)

def stausfoodPageView(request):
    return render(request, 'users/food_status.html')

def siginPageView(request):
    return render(request, 'users/signin.html')

