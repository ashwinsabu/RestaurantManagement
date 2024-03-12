from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPageView, name='index'),
    path('tables/', views.TablePageView, name='tables'),
    path('menu/<int:id>', views.menuPageView, name='menu'),
    path('food_status/<int:id>', views.stausfoodPageView, name='food_status'),
    path('contact/', views.contactPageView, name='contact'),
    path('about/', views.AboutPageView, name='about'),

]