from info import *
def welcome_text():
    print('Welcome to the recommendation system')

def main_menu_text():
    print('''
    
    You are now at the main menu. Please enter 1, 2, or 3 from the following options:
    1. Browse the catalog
    2. Recommendation System
    3. Exit
    
    ''')

def exit_text():
    print('Thank you for using the recommendation system. See you soon!')

def browsing_menu_text():
    print('Welcome to the browsing menu. Here, you can find all the halls in NTU. Enter the option number you wish to get more information on.')
def browsing_menu_catalog():
    print('Here are the options:')
    for i, name in hall_mapping:
        print(i, ": ", name)

    print('If you wish to exit, enter 0')


def recommendation_menu_text():
    print('Welcome to the recommendation menu.')

def req_budget_text():
    print('Input your estimated budget (eg. 350)')

def req_school_text():
    print('Attached are the schools in NTU, input the index number of the school from which your course is from')
    for i, name in school_mapping:
        print(i, ": ", name)

def req_roomtype_text():
    print('Attached are the room types in NTU, input the index number of the room type you prefer')
    for i, name in room_mapping:
        print(i,": ", name)


def req_facilities_text():
    print('Attached are facilities near the halls, input which facilities you want near your hall')
    print('''1. Gym
2. Canteen
3. All of the above
4. None of the above''')

def ranking_text(i = 0):
    if i == 0:
        print('Here are the halls that fulfil all the criteria given')
    if i == 1:
        print('Here are the halls that fulfil all except one of the criteria given')


