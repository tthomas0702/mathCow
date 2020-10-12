#!/usr/bin/env python3

'''
'''

import argparse
import os
import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

### Arguments parsing section ###
def cmd_args():
    """Handles command line arguments given."""
    parser = argparse.ArgumentParser(description='This is a tool for resetting '
                                                 'a repro slot')
    parser.add_argument('-d',
                        '--debug',
                        action='store_true',
                        default=False,
                        help='enable debug')
    parser.add_argument('-n',
                        '--name',
                        action='store',
                        dest='repro_name',
                        #required=True,
                        default='none',
                        help='name used to distinguish the repro')
    parser.add_argument('-s',
                        '--slot',
                        type=int,
                        action='store',
                        dest='slot_id',
                        required=False,
                        #default='100',
                        help='repro slot to restore values 1-4 accepted')


    parsed_arguments = parser.parse_args()

    # debug set print parser info
    if parsed_arguments.debug is True:
        print(parsed_arguments)

    return parsed_arguments

### END ARGPARSE SECTION ###


def run_ssh_copy(device_ip_list):
    'run ssh-copy on the host provided in list'
    for host in device_ip_list:
        command = 'ssh-copy-id -o ConnectTimeout=1 root@{} 2>/dev/null'.format(host)
        os.system(command)

# make function to give Welcome screen


def get_name():
    'Get players name'
    name = input('What is your name? ')

    return name 

def print_large_title(text):
    'Print very large banner'
    cprint(figlet_format(text, font='starwars'),
        'yellow', 'on_red', attrs=['bold'])
    


if __name__ == "__main__":

    SCRIPT_NAME = sys.argv[0]

    OPT = cmd_args()
    #USERNAME = OPT.username

    print_large_title('Math Cow')

    NAME = get_name()

