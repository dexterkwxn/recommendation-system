import random
import constants

sd_list = ["SingleAC","SingleAC","SingleACToilet","SingleNoACToilet","DoubleAC","DoubleNoAC","DoubleACToilet","DoubleNoACToilet"]
cost_list = [[300,330,350,380,400,410],[450,480,510,550,580,600]]
#room type = [S/D, True, True, cost]


def generate_room_type():
    room = []  
    room.append(sd_list[random.randint(0,8)])
    