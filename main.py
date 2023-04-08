import pygame
import helper
import display
from info import *

'''
Browsing Menu
'''
def browsing_menu():
    while True:
        display.browsing_menu_text()
        choice = 0
        while True: #handle errors
            display.browsing_menu_catalog()
            try:
                choice = int(input())
                if choice == 0:
                    return
                if choice not in [i for i, _ in hall_mapping]:
                    print('Enter a valid option')
                break
            except:
                print('Enter a valid option')
        choice = [i[1] for i in hall_mapping if choice in i][0]
        show_hall_info(choice)

def show_hall_info(choice):
    print(f'You have selected {choice}')
    # show information, select to show pic maybe
    print(f'\n{data[choice][name]}:')
    print("Room types available:")
    count = 1
    for room, price in data[choice][rooms]:
        print(f'{count}. {room}, Price: ${price}')
        count += 1
    print('\nFacilities Available in this hall: ')
    if len(data[choice][facilities]) == 0:
        print("None.")
    else:
        for i, fac in enumerate(data[choice][facilities]):
            print(f'{i+1}. {fac}')

    print("Enter anything to go back to the browsing menu.")
    _ = input()
    return


'''
Recommendation Menu
'''
def recommendation_menu():
    display.recommendation_menu_text()
    budget = 0
    school = 0
    roomopt = 0
    facil = 0

    # budget
    display.req_budget_text()
    while True: #error handling
        try:
            budget = float(input())
            if budget > 0:
                break
            else:
                print('Error. Re-input a proper option')
        except:
                print('Error. Re-input a proper option')
    
    # school
    display.req_school_text()
    while True:
        try:
            school = int(input())
            if school in [i for i, _ in school_mapping]:
                break
            else:
                print('Error. Re-input a proper option')
        except:
                print('Error. Re-input a proper option')

    # single vs double
    display.req_roomtype_text()
    while True:
        try:
            roomopt = int(input())
            if roomopt in [i for i, _ in room_mapping]:
                break
            else:
                print('Error. Re-input a proper option')
        except:
                print('Error. Re-input a proper option')            
    room_type = [type for i, type in room_mapping if i == roomopt][0]
   
    # must have facilities
    display.req_facilities_text()
    while True:
        try:
            facil = int(input())
            if facil in [1,2,3,4]:
                break
            else:
                print('Error. Re-input a proper option')
        except:
                print('Error. Re-input a proper option')  

    # actual recommendation algorithm

    # facilities
    facilities_halls = []
    if facil == 1: #Only Gym
        facilities_halls = [v[name] for k, v in data.items() if gym in v[facilities]]
    elif facil == 2: #Only Canteen
        facilities_halls = [v[name] for k, v in data.items() if canteen in v[facilities]]
    elif facil == 3: #Canteen and Gym
        facilities_halls = [v[name] for k, v in data.items() if (gym in v[facilities] and canteen in v[facilities])]
    else: #none of the above
        facilities_halls = [v[name] for k, v in data.items()]

    # room type
    room_type_halls = [v[name] for k, v in data.items() if room_type in [i[0] for i in v[rooms]]]

    # budget
    budget_halls = []
    for k, v in data.items():
        for roomtype, price in v[rooms]:
            if price <= budget:
                budget_halls.append(v[name])
                break

    best_halls = [hall for hall in room_type_halls if (hall in budget_halls and hall in facilities_halls)] #all the halls that fit all the criteria: budget, room type and facilities
    halls_to_map = {}

    #Check for best roomtypes
    halls = [data[hall] for hall in best_halls]
    best_rooms = []

    #best choice
    for hall in halls:
        halls_to_map[hall[name]] = hall_locations[hall[name]]
        item = hall.copy()
        item[rooms] = []
        for j in hall[rooms]:
            if j[0] == room_type and j[1] <= budget:
                item[rooms].append(j)
        best_rooms.append(item.copy())

    # display result
    display.ranking_text(i= 0)
    count = 1
    for i in best_rooms: #to print out results
        school_mapped = [i[1] for i in school_mapping if school in i][0]
        school_coord = school_locations[school_mapped]
        distance = helper.dist(int(school_coord[0]), int(school_coord[1]), int(hall_locations[i[name]][0]), int(hall_locations[i[name]][1]))
        walking_time = distance//walking_rate
        print(f"\n{i[name]} ---\nEstimated Walking time to school: {walking_time} minutes\nFacilities: {i[facilities]}.")
        print("Recommended rooms:")
        for index, item in enumerate(i[rooms]):
            print(f"{index + 1}. {item[0]}, Price: {item[1]}")
        print("")

    print(halls_to_map)
    #to show on map
    helper.show_image('./ntu_map.png', {school_mapped: school_coord}, (255, 0, 0))
    helper.show_image('./ntu_map.png', halls_to_map, (0, 255, 0))

''' 
Main Menu
'''
def main():
    # show init text
    display.welcome_text()

    # main loop
    while True: 
    # give options for browsing or recommendation
        #display main menu text
        display.main_menu_text()
        choice = 0
        while True:
            try:
                choice = int(input())
                if choice not in [1, 2, 3]:
                    print('Enter either 1, 2, or 3')
                break
            except:
                print('Enter either 1, 2, or 3')
        
        if choice == 1:
            browsing_menu()
        elif choice == 2:
            recommendation_menu()
        elif choice == 3:
            display.exit_text()
            return;


main()

# main()