from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Room, Message
from Appventas.models import Avatar

@login_required
def rooms(request):
    rooms = Room.objects.all()
    try:
        avatar=Avatar.objects.filter(user=request.user.id)                    
        filtro=len(avatar)-1
        return render(request, 'rooms.html', {'rooms': rooms,"url":avatar[filtro].imagen.url})
    except:
        return render(request, 'rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    usuarios=User.objects.all()
   

    try:
        avatar=Avatar.objects.filter(user=request.user.id)                    
        filtro=len(avatar)-1
        return render(request, 'room.html', {'room': room, 'messages': messages, "usuarios":usuarios,"url":avatar[filtro].imagen.url})
    except:
        return render(request, 'room.html', {'room': room, 'messages': messages, "usuarios":usuarios})
