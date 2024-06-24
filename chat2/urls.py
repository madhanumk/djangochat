
from django.urls import path
from chat2 import views

urlpatterns = [
    path('',views.list_rooms , name="home"),
    path('chat/<int:pk>',views.chat , name="chat"),
    
]
