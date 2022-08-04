from hotel.models import Room
from.availability import check_availability

def get_available_room(category,form):

    room_list=Room.objects.filter(category=category)

    if form.is_valid():
        data=form.cleaned_data
        
    available_rooms=[]
        
    for room in room_list:
        if check_availability(room, data['check_in'],data['check_out']):
            available_rooms.append(room)

    if len(available_rooms)>0:
        return available_rooms
    else:
        return None