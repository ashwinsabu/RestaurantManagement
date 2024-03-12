from django.urls import path
from . import views

urlpatterns = [
    path('', views.StaffIndex, name='index_staff'),

]