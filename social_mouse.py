#!/usr/bin/python3


'''
This is a mouse that like to talk
version 0.0.2
'''


import os
import sys


## clear screen on u Unix and Windows ## 
os.system('cls' if os.name == 'nt' else 'clear')

## pring title ##
spacer = 50
print('#' * spacer + ' Social Mouse ' + '#' * spacer + '\n\n')

## Intro ##
intro = '''You are walking on a long country road. It's a sunny day and there is a
light pleasant breeze. You see a someone approaching from a long ways
away. As you get closer' you see that it is a friendly looking mouse
that is dressed nicely but not fancy. When the mouse gets within a few
feet it stops and with a smile it looks you in the eye and says...\n\n'''
print(intro)





# topic #1 #:

# Mouse speaking and waits for answer
answer = input('Hello: ')  
acceptable_answers = ['hi', 'hello', 'hey', 'wadup', 'good day', 'good morning', 'good afternoon', 'good evening' ]

if answer.lower() in acceptable_answers:
    print('Nice to meet you!\nMy name is Squeeky Squeek.')

elif answer.lower() == 'squeak':
    print('Oh! You speak squeek!\nCan you speak English so the computer can understand?')
    answer = input()
    acceptable_answers = ['yes', 'sure', 'ok', 'no problem']

    if answer.lower() in acceptable_answers:
        print('Great! We should hang out!')

    else:
        print('I best be getting on with my chores')
        sys.exit('Bye')

else:
    print('I am sorry. I an not sure what {} means'.format(answer))






## get name ##
answer = input('What is your name? :')

NAME = answer

print('Nice to meed you {}'.format(NAME))


