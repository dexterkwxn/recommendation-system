import random
from constants import *
from info import *

sd_list = ['single', 'singleToilet', 'singleAC', 'singleACToilet', 'double', 'doubleToilet', 'doubleAC', 'doubleACToilet']
key_list = ['hall1','hall2','hall3','hall4','hall5','hall6','hall7','hall8','hall9','hall10','hall11','hall12','hall13','hall14','hall15','hall16','hall17','hall18','hall19','hall20','hall21','hall22','hall23',]
cost_list = [[300,330,350,380,400,410],[450,480,510,550,580,600]]
facilities = ['gym', 'canteen']
#room type = [S/D, True, True, cost]


def generate_room_type():
    room = []  
    room.append(sd_list[random.randint(0,7)])
    if "Single" in room[0]:
        room.append(cost_list[1][random.randint(0,5)])
    else:
        room.append(cost_list[0][random.randint(0,5)])

    return room


for [_, key], key_name in zip(hall_mapping, key_list):
    rooms = [generate_room_type() for i in range(5)]
    start = random.randint(0,1)
    print(f'{key_name}: {{')
    print(f'    name: {key_name},')
    print(f'    location: {hall_locations[key]},')
    print(f'    rooms: {rooms},')
    print(f'    facilities: {facilities[random.randint(0,1):random.randint(start,2)]},')
    print(f'}},')