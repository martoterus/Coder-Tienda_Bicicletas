from django.urls import path
from .import views

urlpatterns = [
    path('Canales',views.rooms,name='Canales'),
    path('<slug:slug>/',views.room,name='Canal'),
]