#!/usr/bin/python3

# ver 0.0.1
# by Lily (and a little help from Tim)
import os
import time



SCORE = 0

## Intro ##
os.system('clear')
os.system('figlet "*JERBOA QUIZ*"')
time.sleep(5)

print('welcome to jerboa quiz!\n')

print('what is your name?')

NAME = input()

if NAME == 'Tim':
    print('your teeth are yucky and phanpy hates you but I like your blue eyes!!!!\n')
else:
    print('Nice to meet you {}.\n'.format(NAME))
#####


## Question #1 ##
ANSWER = input('Are jerboas cute? (yes/no): ')
if ANSWER.lower() == 'yes':
    SCORE += 1
    print('yes!you are correct!')
    print('Your score is {}\n'.format(SCORE))
else:
    print('WHATS WRONG WITH YOU {}!?!'.format(NAME))
    print('JERBOAS ARE CUTE')
    print('Your score is {} \n'.format(SCORE))
####


## Question #2 ##
ANSWER = input('Do jerboas hibernate durring the winter? (yes/no): ')
if ANSWER.lower() == 'yes':
    SCORE += 1
    print('yes!you are correct!')
    print('Your score is {}\n'.format(SCORE))
else:
    print('Incorrect {}'.format(NAME))
    print('jerboas hibernate durring the winter')
    print('Your score is {}\n'.format(SCORE))
