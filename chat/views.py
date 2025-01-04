from django.shortcuts import render
import random

# Create your views here.


def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    # print('--------0000000--------' + room_name)
    return render(request, 'chat/chatroom.html', {
        'room_name':room_name
    })