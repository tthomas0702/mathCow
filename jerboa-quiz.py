#!/usr/bin/python3


# by Lily (and a little help from Tim)

import os

SCORE = 0

## Intro ##
os.system('clear')

print('welcome to jerboa quiz!')

print('what is your name?')

NAME = input()

if NAME == 'Tim':
    print('your teeth are yucky and phanpy hates you but I like your blue eyes!!!!')
else:
    print('Nice to meet you {}.'.format(NAME))
#####


## Question #1 ##
ANSWER = input('Are jerboas cute? (yes/no): ')
if ANSWER.lower() == 'yes':
    SCORE += 1
    print('yes!you are correct!')
    print('Your score is {}'.format(SCORE))
else:
    print('WHATS WRONG WITH YOU {}!?!'.format(NAME))
    print('JERBOAS ARE CUTE')

