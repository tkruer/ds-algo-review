import src.binarysearch
from src import binarysearch

def display_options():
    print('Choose from the following actions: ')
    action_menu = '''
    Root (R)
    Retrieve account details (RAD)
    Create account funding source (CAFS)
    Create account VAN (CAVAN)
    List account funding sources (LAFS)
    List and search account transfers (LASAT)
    List account mass payments (LAMP)
    Create receive only customer (CROC)
    Create unverified customer (CUVC)
    Create verified personal customer (CVP)
    Retrieve customer (RC)
    List and search customers (LASC)
    Update customer (UC)
    List customer business classifications (LCBC)
    retrieve business classification (RBC)
    initiate KBA (IKBA)
    retrieve KBA (RKBA)
    verify KBA (VKBA)
    Create beneficial owner (CBO)
    Retrieve beneficial owner (RBO)
    list beneficial owners (LBO)
    update beneficial owner (UBO)
    Remove beneficial owner (DBO)
    Retrieve beneficial ownership status (RBOS)
    Certify beneficial ownership (CBOS)
    Quit (Q)
    '''
    print(action_menu)

def get_user_input():
    return input('Enter your action: ')

def handle_input(input):

    if input == 'recBinarySearchArray':
        recBinarySearchArray = [1, 2, 3, 4, 5]
        recBinarySearchTarget = 3
        src.binarysearch.recursivebinarysearch(recBinarySearchArray, recBinarySearchTarget)

    elif input == 'Q':
        quit()