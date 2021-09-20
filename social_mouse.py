#!/usr/bin/python3

'''
This is a mouse that like to talk. Try and keep the conversion 
going as long as possible!
version 0.0.3.L
'''

import os
import sys
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_title(text_string, spacer):
    print('#' * spacer + ' ' + text_string + ' ' + '#' * spacer + '\n\n')
 

## scene 1 ##
def scene_1_intro():
    print('You are walking on a long country road. It\'s a sunny day and there is a ' 
          'light pleasant breeze. You see a someone approaching from a long ways '
          'away. As you get closer you see that it is a friendly looking mouse '
          'that is dressed nicely but not fancy. When the mouse gets within a few '
          'feet it stops and with a smile it looks you in the eye and says...\n\n')

def scene_2_intro():
    print('The mouse look like it wants to ask a question but it is a little embarrased.')
    sleep(1)
    print('It looks around and shifts from foot to foot...')
    sleep(1)
    print('You notice that it is carrying school books and a lunch pale')
    sleep(1)


def ask_question(question, answer_list, correct_response, incorrect_response):
    result = {'response': '', 'correct': False}
    answer = input('{}?: '.format(question))
    if answer.lower() in answer_list:
        result['response'] = correct_response
        result['correct'] = True   
        return result
    else:
        result['response'] = incorrect_response
        result['correct'] = False   
        return result


def sleep(seconds):
    time.sleep(seconds)

print('END OF PROGRAMMING...HALTING PERSONALITY...')

if __name__ == "__main__":
    print('In Main')
    clear_screen()
    print_title('Social Mouse', 50)

    ### scene 1 ####
    scene_1_intro()
    QUESTION = "Hi Their"
    ANSWER_LIST = ['hi', 'hey', 'wad up', 'hello', 'ola']
    CORRECT_RESPONSE = 'Nice to meet you my name is [NEED TO NAME MOUSE]'
    INCORRECT_RESPONSE = 'I am sorry, I do not understand.'
    # run ask_question function and save return dict to RESULT
    RESULT = ask_question(QUESTION, ANSWER_LIST, CORRECT_RESPONSE, INCORRECT_RESPONSE)
    print(RESULT['response'])
    while RESULT['correct'] == False:
        RESULT = ask_question(QUESTION, ANSWER_LIST, CORRECT_RESPONSE, INCORRECT_RESPONSE)
        if RESULT['correct'] == True:
            print(RESULT['response'])

    NAME = input('What is your name? ')
    print('Nice to meet you {}!'.format(NAME))
    sleep(5)

    ### scene 2 ###
    clear_screen()
    print_title('math Help', 50)
    scene_2_intro()
    sleep(3)
    # Ask for math help
    QUESTION = "Will you help me with a math question from school? "
    ANSWER_LIST = ['yes']
    CORRECT_RESPONSE = 'Thank you! Let me find one that is hard for my mouse brain. '
    INCORRECT_RESPONSE = 'OK, I better go home and get help from my mom. Bye!'
    RESULT = ask_question(QUESTION, ANSWER_LIST, CORRECT_RESPONSE, INCORRECT_RESPONSE)
    if RESULT['correct'] == True:
        print(RESULT['response'])
    else:
        print(RESULT['response'])
        sleep(3)
        print('You watch as the mouse walks happlily away down the path')
        sleep(5)        
        print('Game Over')
        sys.exit()

