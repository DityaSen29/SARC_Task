from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('congrats/', views.congrats, name='congrats'),
    path('try-again/', views.try_again, name='try_again'),
]
