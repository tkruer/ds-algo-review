import src.binarysearch
from src import binarysearch

def display_options():
    print('Choose from the following actions: ')
    action_menu = '''
    Binary Search (BS)
    Exit (Q)
    '''
    print(action_menu)

def get_user_input():
    return input('Enter your action: ')

def handle_input(input):

    if input == 'BS':
        ibs_array = [1, 2, 3, 4, 5]
        ibs_target = 3
        print(src.binarysearch.iteractivebinarysearch(array=ibs_array, target=ibs_target))

    elif input == 'Q':
        quit()