from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('routes/', views.routes, name='routes'),
    path('offers/', views.offers, name='offers'),
    path('manage-booking/', views.manage_booking, name='manage_booking'),
]
