from django.shortcuts import render
from .models import Rooms
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def rooms(request):
    rooms=Rooms.objects.all()

    return render(request,'rooms.html',{'rooms':rooms})

@login_required
def room(request,slug):
    canal=Rooms.objects.get(slug=slug)

    return render (request,'room.html',{'canal':canal})