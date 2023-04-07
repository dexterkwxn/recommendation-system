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