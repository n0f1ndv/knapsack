import sys

def get_valid_integer_input(message):
    while True:
        try:
            user_input = input(f'{message}> ')
            number = int(user_input)
            return number

        except ValueError:
            print('Number of nodes MUST be an integer')
            continue
        except KeyboardInterrupt:
            print('\nKeyboardInterrupt')
            sys.exit(1)
        except EOFError:
            sys.exit(1)
            print('EOF detected')