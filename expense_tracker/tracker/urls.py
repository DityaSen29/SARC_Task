from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_money/', views.add_money, name='add_money'),
    path('make_transaction/', views.make_transaction, name='make_transaction'),
]
