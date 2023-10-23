def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_list = []
    for name in names:
        badge_list.append(badge_maker(name))
    return badge_list

def assign_rooms(names):
    room_list = []
    for index, name in enumerate(names):
        room_list.append(f"Hello, {name}! You'll be assigned to room {index+1}!")
    return room_list

def printer(names):
    badge_list = batch_badge_creator(names)
    room_list = assign_rooms(names)
    for badge in badge_list:
        print(badge)
    for room in room_list:
        print(room)
    return None
