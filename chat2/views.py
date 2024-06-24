from django.shortcuts import render
from .models import Room

# Create your views here.



def list_rooms(request):
    rooms = Room.objects.filter(is_active=True)

    print(rooms)

    return render(request, 'home.html', {'rooms':rooms} )


def chat(request,pk):
    room = Room.objects.get(is_active=True,id=pk)



    return render(request, 'chat.html', {'room':room} )
