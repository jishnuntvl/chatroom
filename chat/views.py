from django.shortcuts import render,redirect # type: ignore

from .models import Room,Message # type: ignore

# Create your views here.
def home(request):
    return render(request,'home.html')
def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    msg_obj=Message.objects.filter(room=room_details)
    context={
        'username': username,
        'room': room_details,
        'msg':msg_obj
    }
    return render(request, 'room.html',context )


def checkview(request):
    room=request.POST['room_name']
    username=request.POST['username']
    if not Room.objects.filter(name=room).exists():
        new=Room.objects.create(name=room)
        new.save()
    return redirect('/'+room+'/?username='+username)  
def msgsnd(request,pk,user):
    msg=request.POST['message']
    username=user
    room=Room.objects.get(pk=pk)
    Message.objects.create(value=msg,user=username,room=room).save()
    return redirect('/'+room.name+'/?username='+username)
    

