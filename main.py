# import cv2
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
        while True:
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

        show_hall_info(choice)

def show_hall_info(choice):
    print(f'You have selected {choice}: {data[choice][name]}')
    # show information, select to show pic maybe

    # return once done



'''
Recommendation Menu
'''
def recommendation_menu():
    display.recommendation_menu_text()
    budget = 0
    school = 0
    roomopt = 0
    ac = 0
    facil = 0

    # budget
    display.req_budget_text()
    while True:
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
   
    # must have facilities
    display.req_facilities_text()
    while True:
        try:
            facil = int(input())
            if facil in [1,2,3]:
                break
            else:
                print('Error. Re-input a proper option')
        except:
                print('Error. Re-input a proper option')  

    # actual recommendation algorithm
    results = data
    final = []

    
    # facilities
    facilities_halls = []
    if facil == 1: #Only Gym
        facilities_halls = [v[name] for k, v in data.items() if gym in v[facilities]]
    elif facil == 2: #Only Canteen
        facilities_halls = [v[name] for k, v in data.items() if canteen in v[facilities]]
    else:
        facilities_halls = [v[name] for k, v in data.items() if (gym in v[facilities] and canteen in v[facilities])]

    # room type
    room_type_halls = [v[name] for k, v in data.items() if roomopt in [i[0] for i in v[rooms]]]

    # budget
    budget_halls = []
    for k, v in data.items():
        for roomtype, price in v[rooms]:
            if price <= budget:
                budget_halls.append(v[name])
                break

    best_halls = [hall for hall in room_type_halls if (hall in budget_halls and hall in facilities_halls)]
    runner_up_halls = [hall for hall in room_type_halls if (hall in budget_halls or hall in facilities_halls)]
    runner_up_halls = [hall for hall in runner_up_halls if hall not in best_halls]

    # display result
    

'''
Main Menu
'''
def main():
    # show init text

    # main loop
    while True: 
    # give options for browsing or recommendation
        #display main menu text
        choice = 0
        while True:
            try:
                choice = int(input())
                if choice not in [1, 2]:
                    print('Enter either 1 or 2')
                break
            except:
                print('Enter either 1 or 2')
        
        if choice == 1:
            browsing_menu()
        elif choice == 2:
            recommendation_menu()
        elif choice == 3:
            display.exit_text()
            return;


main()