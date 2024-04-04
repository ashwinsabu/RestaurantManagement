from django.urls import path
from . import views

urlpatterns = [
    path('', views.StaffIndex, name='index_staff'),
    path('menuedit/',views.menuEditPage, name='menuEditPage'),
    path('queries/',views.custQueries, name='custQueries'),
    path('star/',views.StarPageView, name='starEmployee'),
    path('logout/', views.logout_user, name='logout'),

]