import re
import os
import time

MORSE_CODE_DICT = {'A': '.-',
                   'B': '-...',
                   'C': '-.-.',
                   'D': '-..',
                   'E': '.',
                   'F': '..-.',
                   'G': '--.',
                   'H': '....',
                   'I': '..',
                   'J': '.---',
                   'K': '-.-',
                   'L': '.-..',
                   'M': '--',
                   'N': '-.',
                   'O': '---',
                   'P': '.--.',
                   'Q': '--.-',
                   'R': '.-.',
                   'S': '...',
                   'T': '-',
                   'U': '..-',
                   'V': '...-',
                   'W': '.--',
                   'X': '-..-',
                   'Y': '-.--',
                   'Z': '--..',
                   '1': '.----',
                   '2': '..---',
                   '3': '...--',
                   '4': '....-',
                   '5': '.....',
                   '6': '-....',
                   '7': '--...',
                   '8': '---..',
                   '9': '----.',
                   '0': '-----',
                   ',': '--..--',
                   '.': '.-.-.-',
                   '?': '..--..',
                   '!': '-.-.--',
                   '/': '-..-.',
                   '-': '-....-',
                   '(': '-.--.',
                   ')': '-.--.-',
                   '=': '-...-',
                   ':': '---...',
                   ';': '-.-.-.',
                   '+': '.-.-.',
                   }


# Function meant for encryption
def encrypt(message):
    encrypted_text = ''
    for letter in message.upper():
        if letter != ' ':
            try:
                encrypted_letter = MORSE_CODE_DICT[letter] + ' '
            except KeyError:
                # In case there is a symbol/letter in the user input that cannot be found in the Morse alphabet,
                # the letter will be skipped
                pass
            else:
                encrypted_text += encrypted_letter
        else:
            encrypted_text += ' '

    return encrypted_text


# Function to decrypt Morse text
def decrypt(message):
    decrypted_text = ''

    # Splitting a message into parts divided by at least 2 whitespaces
    # Using the "re" built-in python module to work with Regular Expressions
    encrypted_words = re.split(r'\s{2,}', message)
    for word in encrypted_words:
        try:
            # Accessing keys by values in Morse alphabet using the one-liner code
            eng_letter_word = [list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_symbol)] for
                           morse_symbol in word.split()]
        except KeyError:
            # In case a Morse symbol cannot be found in the alphabet, the letter will be skipped
            pass
        else:
            decrypted_text += ''.join(eng_letter_word) + ' '

    return decrypted_text


while True:
    title = '''
    ╔╦╗┌─┐┬─┐┌─┐┌─┐               
    ║║║│ │├┬┘└─┐├┤                
    ╩ ╩└─┘┴└─└─┘└─┘               
    ╔═╗┌─┐┌┬┐┌─┐                  
    ║  │ │ ││├┤                   
    ╚═╝└─┘─┴┘└─┘                  
    ╔╦╗┬─┐┌─┐┌┐┌┌─┐┬  ┌─┐┌┬┐┌─┐┬─┐
     ║ ├┬┘├─┤│││└─┐│  ├─┤ │ │ │├┬┘
     ╩ ┴└─┴ ┴┘└┘└─┘┴─┘┴ ┴ ┴ └─┘┴└─                                                                                                                                                                  
    '''
    os.system('clear')
    user_input = input(f'{title}\nPlease choose one of the options:\n\n   E - Encrypt\n   D - Decrypt\n   Q - Quit the program\n\n')

    if user_input.lower() == 'e':
        os.system('clear')
        user_message = input(f'{title}\nPlease type in the message you want to encrypt:\n\n')

        os.system('clear')
        print(f'{title}\nHere is your encrypted text:\n\n{encrypt(user_message)}\n\n\n\n\n\n\nPress ENTER to go back to the main menu.')
        input()

    elif user_input.lower() == 'd':
        os.system('clear')
        user_message = input(f'{title}\nPlease type in the message you want to decrypt:\n\n')

        os.system('clear')
        print(f'{title}\nHere is your decrypted text:\n\n{decrypt(user_message)}\n\n\n\n\n\n\nPress ENTER to go back to the main menu.')
        input()
    elif user_input.lower() == 'q':
        for dots in ['', '.', '..', '...']*2:
            os.system('clear')
            print(f'{title}\nQuitting the program{dots}')
            time.sleep(0.15)

        os.system('clear')
        break
    else:
        os.system('clear')
        print(f'{title}\nInvalid input. Please try again.')
        input()
