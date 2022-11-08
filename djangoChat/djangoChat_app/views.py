from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import Message,Room

# Create your views here.

# HOME PAGE
def home(request):
    return render(request,'home.html')

def room(request,room,username):
    print("--------------ROOM/In ROOM Function ",room)
    # username = request.GET.get('username')
    # username = request.POST.get('username')

    print("-------USERNAME/In ROOM func------------- ",username)
    room_details = Room.objects.get(name=room)
    print("----------//-----USERNAME ",username,room_details)
    return render(request,'room.html',{
        'username' : username,
        'room' : room,
        'room_details' : room_details
    }
    )   

def checkview(request):
    print("In checkview function")
    room = request.POST.get('room')
    username = request.POST.get('username')
    # print("--------------- ",room,username)

    if Room.objects.filter(name=room).exists():
            # return redirect('/'+room +'/?username='+username)
            return redirect(f'/room/{room}/{username}')
            # return redirect ('/checkview/')
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect(f'/room/{room}/{username}')
    


def send(request):
    print("------------------------In SEND Func")
    username = request.POST['username']
    room_id = request.POST['room_id']
    message = request.POST['message']
    print("---------send-------- ",username,room_id,message)
    new_message = Message.objects.create(value=message,user=username,room=room_id)
    new_message.save
    return HttpResponse("Meassage sent!")


def getMessages(request,room):
    print("____________________In getMessages Fun")
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    # print("-----------------------messages--------------- ",list(messages.values()))
    return JsonResponse({'messages':list(messages.values())})