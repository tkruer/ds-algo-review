from src import binarysearch
from resources import helpers
import os

exit = False


def main():
    while not exit:
        display_options()
        input = get_user_input()
        if input == 'exit':
            exit = True
        else:
            handle_input(input, DWOLLA_APP_KEY, DWOLLA_APP_SECRET)



if __name__ == '__main__':
    recBinarySearchArray = [1, 2, 3, 4, 5]



