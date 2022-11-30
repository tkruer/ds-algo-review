from resources import helpers

def main():
    helpers.display_options()
    input = helpers.get_user_input()
    if input == 'exit':
        exit()
    else:
        helpers.handle_input(input)

if __name__ == '__main__':
    main()


