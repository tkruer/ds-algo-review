from resources import helpers



def main():
    exit = False
    while not exit:
        helpers.display_options()
        input = helpers.get_user_input()
        if input == 'exit':
            exit = True
        else:
            helpers.handle_input(input)



if __name__ == '__main__':
    main()



