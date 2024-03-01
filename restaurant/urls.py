from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPageView, name='index'),
    path('tables/', views.TablePageView, name='tables'),
    path('menu/', views.menuPageView, name='menu'),
    path('food_status/', views.stausfoodPageView, name='food_status'),
    path('sigin/', views.siginPageView, name='sigin'),

]