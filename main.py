import cv2
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
    print(f'You have selected {choice}.{data[choice]}')
    # show information, select to show pic maybe

    # return once done



'''
Recommendation Menu
'''
def recommendation_menu():
    display.recommendation_menu_text()

    # budget

    # course

    # single vs double

    # air con

    # must have facilities

    # actual recommendation algorithm


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