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
    print('Input your estimated budget')

def req_school_text():
    print('Attached are the schools in NTU, input the index number of the school from which your course is from')
    print('''1. Nanyang Business School (NBS)
2. School of Chemistry, Chemical Engineering and Biotechnology (CCEB)
3. School of Electrical and Electronic Engineering (EEE)
4. School of Civil and Environmental Engineering (CEE)
5. School of Materials Science and Engineering (MSE)
6. School of Computer Science and Engineering (SCSE)
7. School of Mechanical and Aerospace Engineering (MAE)
8. School of Humanities (SOH)
9. School of Art, Design and Media (ADM)
10. Wee Kim Wee School of Communication and Information (WKWSCI)
11. School of Social Sciences (SSS)
12. School of Physical and Mathematical Sciences (SPMS)
13. School of Biological Sciences (SBS)
14. The Asian School of the Environment (ASE)
15. Lee Kong Chian School of Medicine
16. National Institute of Education (NIE), Singapore
17. S. Rajaratnam School of International Studies (RSIS)''')


def req_roomtype_text():
    print('Input your desired room type (Single/Double)')

def req_aircon_text():
    print('Input choice of aircon (Y/N)')

def req_facilities_text():
    print('Attached are facilities near the halls, input the index option')
    print('''1. Gym
2. Canteen
3. All of the above''')
