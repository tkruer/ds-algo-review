import src.binarysearch, src.linkedlist
import time


def display_options():
    print('Choose from the following actions: ')
    action_menu = '''
    Binary Search (BS)
    Linear Search (LS)
    Merge Sort (MS)
    Bubble Sort (BBS)
    
    Exit (exit)
    '''
    print(action_menu)

def get_user_input():
    return input('Enter your action: ')
1
def handle_input(input):

    if input == 'BS':
        start_time = time.time()
        print(src.binarysearch.iteractivebinarysearch(array=[1, 2, 3, 4, 5], target=3), (time.time() - start_time))
    elif input == 'LS':
