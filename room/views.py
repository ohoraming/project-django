from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from scheduler.models import Room, UserInRoom
from scheduler.forms import RoomForm

def path_type(request):
    if request.path.split('/')[-1] == 'room':
        return 'Room'
    elif str.isdecimal(request.path.split('/')[-1]) and request.path.split('/')[-2] == 'enter':
        return 'scheduler'

# Create your views here.
@api_view(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        roomForm = RoomForm
        context = {
            'path_type': path_type(request),
            'roomForm': roomForm
        }
        return render(request, 'scheduler/room/create.html', context)
    elif request.method == 'POST':
        title = request.POST['title']
        master = request.POST['master']
        
        room = Room(
            master=master,
            title=title,
        )

        room.save()
        
        userInRoom = UserInRoom(
            room_num=room.pk,
            user_num=master,
        )
        
        userInRoom.save()
        
        return redirect('index')
    
@api_view(['POST'])
def join_room(request, room_num):
    user_num = request.POST['user_num']
    
    if UserInRoom.objects.filter(user_num=user_num).exists():
        return redirect('index')
    
    user_in_room = UserInRoom(
        user_num = user_num,
        room_num = room_num
    )
    
    user_in_room.save()
    
    return redirect('/?success=2')

@api_view(['POST'])
def out_room(request, room_num):
    user_num = request.POST['user_num']
    
    UserInRoom.objects.filter(user_num=user_num).delete()
    
    return redirect('/?success=3')
    
@api_view(['POST'])
def delete(request, room_num):
    room = Room.objects.filter(num=room_num)
    
    uir = UserInRoom.objects.filter(room_num=room_num)
    
    room.delete()
    uir.delete()
    
    return redirect('index')
    
@api_view(['GET'])
def enter_room(request, room_num):
    context = {
        'path_type': path_type(request),
        'room_num': room_num
    }
    return render(request, 'scheduler/schedule.html', context)