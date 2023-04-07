import random
from constants import *

sd_list = [single, singleToilet, singleAC, singleACToilet, double, doubleToilet, doubleAC, doubleACToilet]
cost_list = [[300,330,350,380,400,410],[450,480,510,550,580,600]]
#room type = [S/D, True, True, cost]


def generate_room_type():
    room = []  
    room.append(sd_list[random.randint(0,7)])
    if "Single" in room[0]:
        room.append(cost_list[1][random.randint(0,5)])
    else:
        room.append(cost_list[0][random.randint(0,5)])

    return room