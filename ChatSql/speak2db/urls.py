from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('connect/', views.dbconnect, name='dbconnect'),
    path('chat/', views.chat, name='chat'),
]