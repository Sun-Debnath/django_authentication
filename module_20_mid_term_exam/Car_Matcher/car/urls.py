from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    
    path('add/', views.add_car, name='add_post'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car'),
    path('details/bye/<int:id>/', views.ByeNow, name='detail_bye'),
]
